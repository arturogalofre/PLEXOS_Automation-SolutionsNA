import duckdb
import os
from datetime import datetime

print("Pre-Sim script running successfully")

# Paths (fall back to sane defaults if env vars missing)
simulation_path = os.environ.get('simulation_path', "/simulation")
output_path = os.environ.get('output_path', "/output")

database_file_path = os.path.join(simulation_path, "reference.db")
report_path = os.path.join(output_path, "system_overview.md")

def md_table(headers, rows):
    """Return a Markdown table string given headers (list) and rows (list of tuples)."""
    if not headers:
        return ""
    # Header
    lines = ["| " + " | ".join(str(h) for h in headers) + " |"]
    # Separator
    lines.append("| " + " | ".join("---" for _ in headers) + " |")
    # Rows
    for r in rows:
        lines.append("| " + " | ".join("" if v is None else str(v) for v in r) + " |")
    return "\n".join(lines)

try:
    with duckdb.connect() as con:
        con.execute("INSTALL sqlite;")
        con.execute("LOAD sqlite;")

        print(f"Configuring DuckDB to read existing SQLite database: {database_file_path}")
        con.execute(f"ATTACH '{database_file_path}' (TYPE SQLITE);")
        con.execute("USE reference;")

        # ---------- Queries ----------
        print("Querying database…")

        # 1) Memberships (same shape as your CSV)
        memberships_sql = """
            SELECT
                cl1.Name AS parent_class,
                cl2.Name AS child_class,
                col.Name AS collection,
                obj1.Name AS parent_object,
                obj2.Name AS child_object,
                '' AS subcollection_name
            FROM t_membership mem
            INNER JOIN t_object     obj1 ON obj1.object_id = mem.parent_object_id
            INNER JOIN t_object     obj2 ON obj2.object_id = mem.child_object_id
            INNER JOIN t_collection col  ON col.collection_id = mem.collection_id
            INNER JOIN t_class      cl1  ON cl1.class_id = mem.parent_class_id
            INNER JOIN t_class      cl2  ON cl2.class_id = mem.child_class_id
        """
        memberships_df = con.execute(memberships_sql).fetchdf()
        memberships_rows = [tuple(x) for x in memberships_df.itertuples(index=False, name=None)]
        memberships_headers = ["parent_class", "child_class", "collection", "parent_object", "child_object", "subcollection_name"]

        # 2) Object counts by class
        obj_counts_sql = """
            SELECT c.Name AS class, COUNT(*) AS object_count
            FROM t_object o
            JOIN t_class  c ON c.class_id = o.class_id
            GROUP BY c.Name
            ORDER BY object_count DESC, c.Name
        """
        obj_counts = con.execute(obj_counts_sql).fetchall()
        obj_counts_hdr = ["class", "object_count"]

        # 3) Membership counts by collection (what’s hooked to what)
        memb_counts_sql = """
            SELECT col.Name AS collection, COUNT(*) AS membership_count
            FROM t_membership m
            JOIN t_collection col ON col.collection_id = m.collection_id
            GROUP BY col.Name
            ORDER BY membership_count DESC, col.Name
        """
        memb_counts = con.execute(memb_counts_sql).fetchall()
        memb_counts_hdr = ["collection", "membership_count"]

        # 4) Quick totals
        totals_sql = """
            SELECT
                (SELECT COUNT(*) FROM t_class)       AS classes,
                (SELECT COUNT(*) FROM t_collection)  AS collections,
                (SELECT COUNT(*) FROM t_object)      AS objects,
                (SELECT COUNT(*) FROM t_membership)  AS memberships
        """
        totals = con.execute(totals_sql).fetchone()
        total_classes, total_collections, total_objects, total_memberships = totals

        # 5) Objects without any memberships (useful sanity check)
        orphans_sql = """
            WITH used AS (
                SELECT parent_object_id AS object_id FROM t_membership
                UNION
                SELECT child_object_id  AS object_id FROM t_membership
            )
            SELECT o.Name AS object, c.Name AS class
            FROM t_object o
            JOIN t_class  c ON c.class_id = o.class_id
            LEFT JOIN used u ON u.object_id = o.object_id
            WHERE u.object_id IS NULL
            ORDER BY c.Name, o.Name
        """
        orphans = con.execute(orphans_sql).fetchall()
        orphans_hdr = ["object", "class"]

        # 6) Top 20 objects by number of memberships (who’s most connected)
        top_connected_sql = """
            WITH all_refs AS (
                SELECT parent_object_id AS object_id FROM t_membership
                UNION ALL
                SELECT child_object_id  AS object_id FROM t_membership
            )
            SELECT o.Name AS object, c.Name AS class, COUNT(*) AS membership_refs
            FROM all_refs r
            JOIN t_object o ON o.object_id = r.object_id
            JOIN t_class  c ON c.class_id = o.class_id
            GROUP BY o.Name, c.Name
            ORDER BY membership_refs DESC, o.Name
            LIMIT 20
        """
        top_connected = con.execute(top_connected_sql).fetchall()
        top_connected_hdr = ["object", "class", "membership_refs"]

        # ---------- Build Markdown ----------
        print(f"Writing Markdown report to {report_path}")
        os.makedirs(output_path, exist_ok=True)

        lines = []
        lines.append(f"# PLEXOS System Overview")
        lines.append("")
        lines.append(f"_Generated: {datetime.utcnow().strftime('%Y-%m-%d %H:%M:%S')} UTC_")
        lines.append("")
        lines.append("## Quick Totals")
        lines.append("")
        lines.append(md_table(
            ["classes", "collections", "objects", "memberships"],
            [(total_classes, total_collections, total_objects, total_memberships)]
        ))
        lines.append("")

        lines.append("## Objects per Class")
        lines.append("")
        lines.append(md_table(obj_counts_hdr, obj_counts))
        lines.append("")

        lines.append("## Memberships per Collection")
        lines.append("")
        lines.append(md_table(memb_counts_hdr, memb_counts))
        lines.append("")

        lines.append("## Most Connected Objects (Top 20)")
        lines.append("")
        lines.append(md_table(top_connected_hdr, top_connected))
        lines.append("")

        # Full membership table (can be long, but mirrors your original export)
        lines.append("## Full Membership Table")
        lines.append("")
        lines.append(md_table(memberships_headers, memberships_rows))
        lines.append("")

        # Optional sanity check section
        lines.append("## Objects Without Any Memberships")
        lines.append("")
        if orphans:
            lines.append(md_table(orphans_hdr, orphans))
        else:
            lines.append("_None found._")
        lines.append("")

        with open(report_path, "w", encoding="utf-8") as f:
            f.write("\n".join(lines))

        # Log a short preview to stdout
        print("Quick totals:", totals)
        print("First 10 memberships:")
        for row in memberships_rows[:10]:
            print(row)

        print(f"Report written to {report_path}")

except Exception as e:
    print('Report generation failed:')
    print(e)
finally:
    print("done")

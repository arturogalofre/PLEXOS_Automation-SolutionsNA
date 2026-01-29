import json
import os
import subprocess
import sys
from datetime import datetime


def run_cli(command_args):
    """Run a CLI command and return (ok, stdout, stderr)."""
    try:
        result = subprocess.run(
            command_args,
            check=True,
            stdout=subprocess.PIPE,
            stderr=subprocess.PIPE,
            text=True,
            shell=True,
        )
        return True, result.stdout, result.stderr
    except subprocess.CalledProcessError as e:
        return False, e.stdout or "", e.stderr or str(e)


def list_solutions(study_id):
    """Return list of solution dicts for the study using pxc."""
    ok, out, err = run_cli([
        "pxc",
        "solution",
        "list",
        "--studyId",
        study_id,
        "--format",
        "json",
    ])
    if not ok:
        raise RuntimeError(f"pxc solution list failed: {err}\n{out}")

    # pxc sometimes prints a leading context line like "Using current context:"; strip non-JSON prefix
    out_str = out.strip()
    json_start = out_str.find("[")
    if json_start > 0:
        out_str = out_str[json_start:]

    try:
        return json.loads(out_str)
    except json.JSONDecodeError as ex:
        raise RuntimeError(f"Failed to parse solution list JSON. Raw output:\n{out}") from ex


def pick_latest_solution(solutions):
    """Pick the most recently updated solution by LastUpdatedDate."""
    if not solutions:
        return None

    def parse_dt(s):
        # Example: 2025-09-18T15:36:00.1845806Z
        return datetime.fromisoformat(s.replace("Z", "+00:00"))

    return max(solutions, key=lambda s: parse_dt(s.get("LastUpdatedDate") or s.get("CreatedDate")))


def download_solution_files(solution_id, out_dir):
    os.makedirs(out_dir, exist_ok=True)
    ok, out, err = run_cli([
        "pxc",
        "solution",
        "files",
        "download",
        "--solutionId",
        solution_id,
        "-d",
        out_dir,
    ])
    if not ok:
        raise RuntimeError(f"pxc solution files download failed: {err}\n{out}")
    return out.strip()


def main(argv=None):
    argv = argv or sys.argv[1:]
    if len(argv) < 2:
        print("Usage: python -m prepost.enqueuers.download_last_solution <STUDY_ID> <OUTPUT_DIR>")
        sys.exit(2)

    study_id = argv[0]
    output_dir = argv[1]

    print(f"Listing solutions for study: {study_id} …")
    solutions = list_solutions(study_id)
    if not isinstance(solutions, list) or not solutions:
        print("No solutions found.")
        sys.exit(1)

    latest = pick_latest_solution(solutions)
    if not latest:
        print("No latest solution could be determined.")
        sys.exit(1)

    sol_id = latest.get("SolutionId")
    sim_id = latest.get("SimulationId")
    exec_id = latest.get("ExecutionId")
    sol_type = latest.get("Type")
    when = latest.get("LastUpdatedDate") or latest.get("CreatedDate")

    print(f"Latest solution: {sol_id} | Type: {sol_type} | Updated: {when} | SimulationId: {sim_id} | ExecutionId: {exec_id}")
    print(f"Downloading to: {output_dir}")
    msg = download_solution_files(sol_id, output_dir)
    print(msg or "Download completed.")


if __name__ == "__main__":
    main()

# PLEXOS Cloud Datahub Connectors - Complete Guide

## Table of Contents

1. [What are Datahub Connectors?](#what-are-datahub-connectors)
2. [Prerequisites](#prerequisites)
3. [Supported Storage Providers](#supported-storage-providers)
4. [Step-by-Step Setup](#step-by-step-setup)
5. [Authentication Methods](#authentication-methods)
6. [Creating Your First Connector](#creating-your-first-connector)
7. [Using Connectors in Practice](#using-connectors-in-practice)
8. [Managing Connectors](#managing-connectors)
9. [Troubleshooting](#troubleshooting)
10. [Best Practices](#best-practices)

---

## What are Datahub Connectors?

**Datahub Connectors** are a powerful feature in PLEXOS Cloud that allows you to seamlessly integrate external cloud storage (Azure Blob Storage and Amazon S3) directly into your PLEXOS workflows.

### Key Benefits

- **No More Manual Transfers**: Access files in external storage as if they were native to PLEXOS Cloud
- **Streamlined Workflows**: Reference external datasets directly in simulations and analysis
- **Cost Efficiency**: Avoid duplicating large datasets in PLEXOS Cloud storage
- **Security**: Maintain tenant-level control and security policies
- **Scalability**: Handle massive datasets without storage limitations

### How It Works

Once configured, connectors create a bridge between PLEXOS Cloud and your external storage. Files in connected storage appear as extensions of your Datahub, accessible through standard PLEXOS CLI commands.

---

## Prerequisites

### 1. PLEXOS Cloud Access

- Active PLEXOS Cloud account with CLI access
- Administrator privileges (required for feature activation)

### 2. External Storage Accounts

**For Azure Blob Storage:**

- Azure Storage Account
- Container created in your storage account
- Appropriate permissions (read/write access)

**For Amazon S3:**

- AWS Account with S3 access
- S3 bucket created
- IAM permissions for the bucket

### 3. Authentication Credentials

- Access keys, connection strings, or tokens for your chosen storage provider
- Understanding of your organization's security policies

### 4. PLEXOS CLI

- PXC CLI installed and configured
- Familiarity with basic CLI commands

---

## Supported Storage Providers

### Azure Blob Storage

Microsoft's cloud object storage service, ideal for:

- Large unstructured datasets
- Enterprise environments with Azure infrastructure
- Organizations already using Azure ecosystem

### Amazon S3

AWS's object storage service, perfect for:

- Cross-platform compatibility
- Organizations using AWS infrastructure
- High scalability requirements

---

## Step-by-Step Setup

### Step 1: Enable Connectors Feature (Admin Only)

As a tenant administrator, you must first activate the connectors feature:

```bash
# Check current status
pxc datahub connector feature-status

# Enable connectors for your tenant
pxc datahub connector feature --activate true

# Verify activation
pxc datahub connector feature-status
```

**Expected Output:**

```
Feature Status: Enabled
```

### Step 2: Verify Your Storage Credentials

Before creating connectors, ensure you have the correct credentials:

**Azure Blob Storage:**

- Connection String, OR
- Account Name + Account Key, OR
- SAS Token, OR
- Service URI for token-based auth

**Amazon S3:**

- Access Key ID + Secret Access Key
- Region and bucket name
- Optional: Session tokens or role ARN for advanced auth

### Step 3: Create Your First Connector

Choose your storage provider and authentication method, then create the connector.

---

## Authentication Methods

### Azure Blob Storage Authentication

| Method               | Use Case                   | Required Parameters                                            |
| -------------------- | -------------------------- | -------------------------------------------------------------- |
| **ConnectionString** | Simple setup, full access  | `connection-string`, `container-name`                          |
| **SharedKey**        | Direct key-based auth      | `service-uri`, `account-name`, `account-key`, `container-name` |
| **SAS**              | Limited, time-bound access | `service-uri`, `sas-token`, `container-name`                   |
| **Token**            | Azure AD integration       | `service-uri`, `container-name`                                |

### Amazon S3 Authentication

| Method           | Use Case              | Required Parameters                                                                   |
| ---------------- | --------------------- | ------------------------------------------------------------------------------------- |
| **AccountCreds** | Standard AWS access   | `s3-access-key`, `s3-secret-key`, `region`, `bucket-name`                             |
| **SharedKey**    | Temporary credentials | `s3-access-key`, `s3-secret-key`, `session-token`, `region`, `bucket-name`            |
| **AssumeRole**   | Cross-account access  | `s3-access-key`, `s3-secret-key`, `role-arn`, `session-name`, `region`, `bucket-name` |

---

## Creating Your First Connector

### Azure Blob Storage Connector

#### Using Connection String (Recommended for simplicity):

```bash
pxc datahub connector create \
  --name "my-azure-storage" \
  --connector-type AzureBlob \
  --auth-type ConnectionString \
  --connection-string "DefaultEndpointsProtocol=https;AccountName=youraccount;AccountKey=yourkey;EndpointSuffix=core.windows.net" \
  --container-name "my-container"
```

#### Using SAS Token (Recommended for security):

```bash
pxc datahub connector create \
  --name "my-azure-secure" \
  --connector-type AzureBlob \
  --auth-type SAS \
  --service-uri "https://youraccount.blob.core.windows.net" \
  --sas-token "your-sas-token-here" \
  --container-name "my-container"
```

### Amazon S3 Connector

#### Using Account Credentials:

```bash
pxc datahub connector create \
  --name "my-s3-storage" \
  --connector-type AmazonS3 \
  --auth-type AccountCreds \
  --s3-access-key "AKIAIOSFODNN7EXAMPLE" \
  --s3-secret-key "wJalrXUtnFEMI/K7MDENG/bPxRfiCYEXAMPLEKEY" \
  --region "us-east-1" \
  --bucket-name "my-bucket"
```

#### Using AssumeRole (Advanced):

```bash
pxc datahub connector create \
  --name "my-s3-role" \
  --connector-type AmazonS3 \
  --auth-type AssumeRole \
  --s3-access-key "AKIAIOSFODNN7EXAMPLE" \
  --s3-secret-key "wJalrXUtnFEMI/K7MDENG/bPxRfiCYEXAMPLEKEY" \
  --role-arn "arn:aws:iam::123456789012:role/MyRole" \
  --session-name "PlexosSession" \
  --region "us-east-1" \
  --bucket-name "my-bucket"
```

### Verify Connector Creation

```bash
# List all connectors
pxc datahub connector list
```

**Expected Output:**

```
Name: my-azure-storage
Type: AzureBlob
Auth Type: ConnectionString
Status: Active

Name: my-s3-storage
Type: AmazonS3
Auth Type: AccountCreds
Status: Active
```

---

## Using Connectors in Practice

### Understanding Connector Paths

All connector access uses a standardized path format:

```
connectors/<ConnectorType>/<ConnectorName>/<YourFiles>
```

**Examples:**

- `connectors/AzureBlob/my-azure-storage/data/input.csv`
- `connectors/AmazonS3/my-s3-storage/results/output.xlsx`

### Basic Operations

#### Upload Files to Connected Storage

```bash
# Upload a single file
pxc datahub upload \
  --local-path "C:\my-files\input-data.csv" \
  --remote-path "connectors/AzureBlob/my-azure-storage/input/input-data.csv"

# Upload an entire folder
pxc datahub upload \
  --local-folder "C:\my-project\data" \
  --remote-folder "connectors/AmazonS3/my-s3-storage/project-data"
```

#### Download Files from Connected Storage

```bash
# Download a specific file
pxc datahub download \
  --remote-path "connectors/AzureBlob/my-azure-storage/results/model-output.csv" \
  --local-path "C:\downloads\model-output.csv"

# Download to a folder
pxc datahub download \
  --remote-path "connectors/AmazonS3/my-s3-storage/**" \
  --local-folder "C:\downloads\s3-data"
```

#### Search and Browse Connected Storage

```bash
# List all files in a connector
pxc datahub search --path "connectors/AzureBlob/my-azure-storage/**"

# Search for specific file types
pxc datahub search --path "connectors/AmazonS3/my-s3-storage/**/*.csv"

# Search within a specific folder
pxc datahub search --path "connectors/AzureBlob/my-azure-storage/data/**"
```

### Integration with PLEXOS Workflows

Connectors integrate seamlessly with existing PLEXOS commands:

```bash
# Reference connector files in simulations
pxc simulation run \
  --input-data "connectors/AzureBlob/my-azure-storage/input/dataset.csv" \
  --output-dir "connectors/AmazonS3/my-s3-storage/results"

# Use in analysis workflows
pxc analysis create \
  --data-source "connectors/AzureBlob/my-azure-storage/historical-data" \
  --output "connectors/AmazonS3/my-s3-storage/analysis-results"
```

---

## Managing Connectors

### Update Connector Configuration

```bash
# Update authentication credentials
pxc datahub connector update \
  --name "my-azure-storage" \
  --auth-type SAS \
  --sas-token "new-sas-token-here"
```

### Remove Connectors

```bash
# Delete a connector
pxc datahub connector delete --name "my-azure-storage"

# Note: This only removes the connection, not the actual storage
```

### Monitor Connector Status

```bash
# List all connectors with status
pxc datahub connector list

# Check feature status
pxc datahub connector feature-status
```

---

## Troubleshooting

### Authentication Issues

**Problem:** "Authentication failed" or "Access denied"
**Solutions:**

- Verify credentials are correct and not expired
- Check that your account has appropriate permissions
- For Azure: Ensure container exists and is accessible
- For S3: Verify bucket permissions and region settings

**Problem:** "Invalid connection string"
**Solutions:**

- Double-check the connection string format
- Ensure no extra spaces or encoding issues
- Test connection string in Azure Storage Explorer first

### Path and File Issues

**Problem:** "Path not found" errors
**Solutions:**

- Use correct path format: `connectors/<Type>/<Name>/<Path>`
- Ensure connector name matches exactly (case-sensitive)
- Verify files exist in external storage

**Problem:** Upload/download failures
**Solutions:**

- Check network connectivity
- Verify file permissions in external storage
- Ensure sufficient storage quota

### Feature Activation Issues

**Problem:** "Feature not enabled" or "Command not found"
**Solutions:**

- Ensure you're using administrator account
- Run: `pxc datahub connector feature --activate true`
- Verify with: `pxc datahub connector feature-status`

### Network and Connectivity

**Problem:** Connection timeouts
**Solutions:**

- Check firewall settings
- Verify internet connectivity
- For corporate networks: Check proxy settings
- Test direct access to storage endpoints

---

## Best Practices

### Security

1. **Use appropriate authentication methods:**

   - SAS tokens for time-limited access
   - IAM roles for cross-account access
   - Avoid storing credentials in scripts

2. **Follow principle of least privilege:**
   - Grant minimum required permissions
   - Use read-only access when possible

### Organization

3. **Use descriptive connector names:**

   - `production-azure-east` instead of `azure1`
   - Include environment and region information

4. **Structure your storage logically:**
   - Group related files in folders
   - Use consistent naming conventions

### Performance

5. **Optimize file operations:**
   - Upload/download in batches when possible
   - Use search commands to verify paths before operations
   - Consider file size limits for your storage provider

### Maintenance

6. **Regular credential rotation:**

   - Update SAS tokens before expiration
   - Rotate access keys periodically
   - Monitor connector usage and access patterns

7. **Documentation:**
   - Maintain records of connector configurations
   - Document authentication methods used
   - Keep track of who has access to what

### Integration

8. **Incorporate into workflows:**
   - Reference connector paths in scripts and automation
   - Use consistent path structures across projects
   - Plan for connector dependencies in workflows

---

## Quick Start Checklist

- [ ] Enable connectors feature (admin only)
- [ ] Prepare storage credentials
- [ ] Create connector with appropriate auth method
- [ ] Test connection with search command
- [ ] Upload test file
- [ ] Download test file
- [ ] Integrate into PLEXOS workflows

## Support and Resources

- **PLEXOS Cloud Documentation**: Comprehensive guides and API references
- **CLI Help**: `pxc datahub connector --help` for command details
- **Community Forums**: Connect with other PLEXOS users
- **Support Portal**: Official PLEXOS Cloud support channels

---

_This guide combines official PLEXOS Cloud documentation with practical CLI usage examples to provide a complete reference for implementing Datahub Connectors in your environment._

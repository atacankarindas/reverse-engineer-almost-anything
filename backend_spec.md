# Backend Specification

## Objective

Build a metadata-driven backend platform capable of generating and operating configurable business applications.

The backend must support:

- Dynamic forms
- Dynamic grids
- Metadata management
- Security
- Audit logging
- Workflow configuration
- Oracle integration
- Power BI integration

The platform should avoid hardcoded application logic and instead derive behavior from metadata.

---

# Technology Stack

## API Framework

- FastAPI

## ORM

- SQLAlchemy 2.x

## Validation

- Pydantic

## Authentication

- Microsoft Entra ID

## Database

Platform Metadata:

- PostgreSQL

Business Data:

- Oracle Database

---

# Architecture Principles

## Metadata Driven

Business applications are defined through metadata.

Example:

BusinessCase
    ↓
Widget Definitions
    ↓
Validation Rules
    ↓
Permissions
    ↓
Generated UI

Backend should expose metadata APIs that allow the frontend to generate screens dynamically.

---

# Core Domains

## BusinessCase

Represents a configurable application.

Responsibilities:

- Metadata ownership
- Widget ownership
- Security ownership
- Workflow ownership

---

## Widget

Represents a configurable UI component.

Responsibilities:

- Field definitions
- Layout definitions
- Validation mappings

---

## Connection

Represents an Oracle data source.

Responsibilities:

- Database connectivity
- Schema discovery
- Table discovery
- View discovery

---

## Security

Responsibilities:

- Authentication
- Authorization
- Role mapping
- Permission evaluation

---

## Workflow

Responsibilities:

- Workflow definitions
- Workflow states
- Workflow transitions

---

## Audit

Responsibilities:

- Change tracking
- User activity tracking
- Data history

---

# Metadata Schema

## business_case

```sql
business_case
(
    id uuid,
    name varchar,
    description varchar,
    status varchar,
    connection_id uuid,
    created_at timestamp,
    updated_at timestamp
)
```

---

## widget

```sql
widget
(
    id uuid,
    business_case_id uuid,
    field_name varchar,
    widget_type varchar,
    label varchar,
    position integer,
    required boolean,
    visible boolean
)
```

---

## validation_rule

```sql
validation_rule
(
    id uuid,
    widget_id uuid,
    rule_type varchar,
    expression text,
    message text
)
```

---

## security_group

```sql
security_group
(
    id uuid,
    name varchar,
    description varchar
)
```

---

## workflow_definition

```sql
workflow_definition
(
    id uuid,
    business_case_id uuid,
    name varchar,
    status varchar
)
```

---

# Oracle Integration Layer

## Purpose

Enable dynamic discovery of Oracle structures.

---

## Schema Discovery

```sql
SELECT owner
FROM all_users
```

---

## Table Discovery

```sql
SELECT owner,
       table_name
FROM all_tables
```

---

## View Discovery

```sql
SELECT owner,
       view_name
FROM all_views
```

---

## Column Discovery

```sql
SELECT column_name,
       data_type,
       nullable
FROM all_tab_columns
```

---

## Primary Key Discovery

```sql
SELECT cols.table_name,
       cols.column_name
FROM all_constraints cons
JOIN all_cons_columns cols
ON cons.constraint_name = cols.constraint_name
WHERE cons.constraint_type = 'P'
```

---

# Dynamic Grid Engine

## Responsibilities

Generate CRUD operations dynamically from metadata.

Input:

```json
{
  "table": "CUSTOMER_MASTER",
  "primaryKey": "CUSTOMER_ID"
}
```

Output:

- Grid definition
- CRUD endpoints
- Validation model

---

## Supported Operations

### Read

Dynamic SELECT generation.

### Insert

Dynamic INSERT generation.

### Update

Dynamic UPDATE generation.

### Delete

Dynamic DELETE generation.

### Bulk Update

Mass update of selected records.

---

# API Design

## Business Cases

### List

```http
GET /api/business-cases
```

---

### Create

```http
POST /api/business-cases
```

---

### Details

```http
GET /api/business-cases/{id}
```

---

### Update

```http
PUT /api/business-cases/{id}
```

---

### Delete

```http
DELETE /api/business-cases/{id}
```

---

# Widgets

```http
GET    /api/widgets
POST   /api/widgets
PUT    /api/widgets/{id}
DELETE /api/widgets/{id}
```

---

# Connections

```http
GET    /api/connections
POST   /api/connections
PUT    /api/connections/{id}
DELETE /api/connections/{id}
```

---

# Dynamic Data APIs

## Data Query

```http
POST /api/data/query
```

Request:

```json
{
  "businessCaseId": "...",
  "filters": []
}
```

---

## Insert Record

```http
POST /api/data/insert
```

---

## Update Record

```http
POST /api/data/update
```

---

## Delete Record

```http
POST /api/data/delete
```

---

## Bulk Update

```http
POST /api/data/bulk-update
```

---

# Security Engine

## Authentication

Microsoft Entra ID

Supported:

- OAuth2
- OpenID Connect

---

## Authorization

Role Based Access Control (RBAC)

Permissions:

- View
- Edit
- Delete
- Administer

Scopes:

- Business Case
- Widget
- Data
- Workflow

---

# Audit Engine

Track:

- User
- Timestamp
- Object
- Action
- Before Value
- After Value

Example:

```json
{
  "user": "ATA24292",
  "object": "CUSTOMER_MASTER",
  "action": "UPDATE",
  "field": "STATUS",
  "oldValue": "ACTIVE",
  "newValue": "PASSIVE"
}
```

---

# Validation Engine

Supported Rule Types

- Required
- Min Length
- Max Length
- Regex
- Numeric Range
- Date Range
- SQL Validation

Execution:

Frontend Validation
    +
Backend Validation

---

# Power BI Integration

## Purpose

Provide maintenance capability for Power BI users.

---

## Deep Link Support

Example:

```text
/apps/customer-management?customer_id=12345
```

---

## Context Parameters

Supported:

- CustomerId
- BookingId
- FlightNumber
- Pnr

---

## Save Workflow

Power BI
    ↓
Open Maintenance Screen
    ↓
Update Oracle
    ↓
Trigger Refresh
    ↓
Updated Dashboard

---

# Performance Requirements

Read Operations:

- < 2 seconds

Grid Filtering:

- < 1 second

CRUD Operations:

- < 3 seconds

Bulk Update:

- 10,000 rows minimum

---

# MVP Scope

Included:

- Oracle Integration
- Metadata Management
- Dynamic Forms
- Dynamic Grids
- Security
- Audit Logging
- Power BI Deep Links

Excluded:

- Custom Workflow Engine
- Multi Database Support
- Advanced Approval Processes
- Graph Database
- AI Assistants

---

# Success Criteria

A business administrator should be able to:

1. Connect Oracle
2. Select a table or view
3. Generate a Business Case
4. Configure Widgets
5. Configure Permissions
6. Open a generated application
7. Read and edit Oracle data
8. Access the application from Power BI

without writing any code.

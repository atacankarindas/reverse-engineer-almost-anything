# Oracle Data Grid Specification

## Objective

Build a metadata-driven Oracle Data Grid Engine capable of automatically generating secure, configurable and high-performance data maintenance applications.

The Oracle Data Grid Engine is the primary business capability of the platform.

Its purpose is to enable business users to maintain Oracle data without writing SQL, building custom applications or involving development teams.

The engine should integrate seamlessly with:

- Oracle Database
- Power BI
- Business Cases
- Security Engine
- Audit Engine

---

# Vision

Traditional Flow

Power BI
↓
Issue Found
↓
Email
↓
Excel File
↓
Data Team
↓
Database Update
↓
Refresh

Target Flow

Power BI
↓
Issue Found
↓
Open Maintenance Screen
↓
Edit Data
↓
Save
↓
Audit Created
↓
Refresh Dataset
↓
Updated Dashboard

---

# Design Principles

## Metadata Driven

The grid should never be manually developed.

Every grid should be generated from metadata.

Source:

Business Case
↓
Oracle Metadata
↓
Grid Configuration
↓
Generated Grid

---

## Oracle First

Version 1 supports Oracle only.

Benefits:

- Reduced complexity
- Faster MVP
- Better metadata discovery
- Strong enterprise adoption

Future releases may support:

- PostgreSQL
- SQL Server

---

## Server-Side Operations

All large data operations must execute within Oracle.

Avoid client-side processing.

Supported server-side operations:

- Filtering
- Sorting
- Pagination
- Aggregation
- Searching

---

# Grid Source Types

## Standard Table

Source:

```sql
APP.CUSTOMER_MASTER
```

Capabilities:

- Read
- Insert
- Update
- Delete

---

## Oracle View

Source:

```sql
APP.V_CUSTOMER_MASTER
```

Capabilities:

- Read

Optional:

- Update through supported Oracle mechanisms

---

## Custom Query

Source:

```sql
SELECT
    customer_id,
    customer_name,
    country
FROM app.customer_master
WHERE active_flag = 'Y'
```

Capabilities:

- Read

Optional:

- Update if update logic is defined

---

# Oracle Discovery Engine

## Purpose

Automatically discover Oracle structures.

The user should never manually define columns if metadata can be discovered.

---

## Schema Discovery

```sql
SELECT username
FROM all_users
```

Output:

- Available schemas

---

## Table Discovery

```sql
SELECT owner,
       table_name
FROM all_tables
```

Output:

- Available tables

---

## View Discovery

```sql
SELECT owner,
       view_name
FROM all_views
```

Output:

- Available views

---

## Column Discovery

```sql
SELECT column_name,
       data_type,
       nullable,
       data_length
FROM all_tab_columns
```

Output:

- Column Name
- Data Type
- Nullable
- Length

---

## Primary Key Discovery

```sql
SELECT
    cols.table_name,
    cols.column_name
FROM all_constraints cons
JOIN all_cons_columns cols
ON cons.constraint_name = cols.constraint_name
WHERE cons.constraint_type = 'P'
```

Output:

- Primary Key Columns

---

## Foreign Key Discovery

```sql
SELECT
    cols.table_name,
    cols.column_name
FROM all_constraints cons
JOIN all_cons_columns cols
ON cons.constraint_name = cols.constraint_name
WHERE cons.constraint_type = 'R'
```

Output:

- Relationships

---

# Business Case Configuration

## Example

```json
{
  "name": "Customer Management",
  "schema": "APP",
  "table": "CUSTOMER_MASTER",
  "primaryKey": "CUSTOMER_ID"
}
```

---

# Column Metadata

Example:

```json
{
  "column": "STATUS",
  "label": "Status",
  "widget": "dropdown",
  "editable": true,
  "required": true,
  "visible": true
}
```

---

# Grid Generation Process

Step 1

Discover Oracle structure

↓

Step 2

Create Business Case

↓

Step 3

Generate Column Metadata

↓

Step 4

Generate Grid

↓

Step 5

Apply Security

↓

Step 6

Enable CRUD Operations

---

# Grid Capabilities

## Read

Generate dynamic queries.

Example:

```sql
SELECT *
FROM CUSTOMER_MASTER
```

---

## Insert

Allow creation of records.

Example:

```sql
INSERT INTO CUSTOMER_MASTER (...)
VALUES (...)
```

---

## Update

Allow modification of records.

Example:

```sql
UPDATE CUSTOMER_MASTER
SET STATUS='ACTIVE'
WHERE CUSTOMER_ID=1001
```

---

## Delete

Allow controlled deletion.

Example:

```sql
DELETE
FROM CUSTOMER_MASTER
WHERE CUSTOMER_ID=1001
```

---

## Copy Record

Allow duplication of records.

Example:

```text
Select Record
↓
Copy
↓
Modify Key Fields
↓
Save
```

---

## Bulk Update

High-value feature.

Example:

```text
1000 Rows Selected

Status = ACTIVE
```

Result:

```sql
UPDATE CUSTOMER_MASTER
SET STATUS='ACTIVE'
WHERE CUSTOMER_ID IN (...)
```

---

# Filtering Engine

## Column Filters

Supported:

- Equals
- Not Equals
- Contains
- Starts With
- Ends With

---

## Numeric Filters

Supported:

- Greater Than
- Less Than
- Between

---

## Date Filters

Supported:

- Before
- After
- Between

---

## Generated SQL Example

```sql
WHERE status = 'ACTIVE'
AND country = 'TR'
```

---

# Sorting Engine

Supported:

- Ascending
- Descending
- Multi Column

Generated SQL:

```sql
ORDER BY country,
         customer_name
```

---

# Pagination Engine

Must be server-side.

Generated SQL:

```sql
OFFSET :offset ROWS
FETCH NEXT :limit ROWS ONLY
```

---

# Search Engine

Global Search

Example:

```text
Atacan
```

Generated SQL:

```sql
WHERE UPPER(customer_name)
LIKE '%ATACAN%'
```

---

# Inline Editing

Users modify cells directly.

Example:

Before

```text
ACTIVE
```

After

```text
PASSIVE
```

Changes remain in memory until Save.

---

# Dirty State Tracking

Track:

```json
{
  "row": 1001,
  "column": "STATUS",
  "old": "ACTIVE",
  "new": "PASSIVE"
}
```

---

# Validation Engine

## Required

```json
{
  "type": "required"
}
```

---

## Length Validation

```json
{
  "type": "max_length",
  "value": 50
}
```

---

## Numeric Range

```json
{
  "type": "range",
  "min": 0,
  "max": 100
}
```

---

## Regex Validation

```json
{
  "type": "regex",
  "pattern": "..."
}
```

---

## SQL Validation

```sql
SELECT COUNT(*)
FROM CUSTOMER_MASTER
WHERE EMAIL*:email
```

Use*Cases*

- Uniqueness Checks
- Business C*nstraints

---

# Audit Engine

Ev*ry change must be audited.

Captur*:

- User
- Timestamp
- Table
- Co*umn
- Old Value
- New Value
- Acti*n

---

## Audit Example

```json
*
  "user": "ATA24292",
  "table": *CUSTOMER_MASTER",
  "column": "STA*US",
  "oldValue": "ACTIVE",
  "ne*Value":*"PASSIVE",
  "timestamp*: "2026-11*12T17:00:00*
}
```

---

#*Security Integration

Grid behavio* must be*permission aware.

Supported*permissions:

## Read

View*records.

##*Insert

Create records.

##*Update

Modify records.

## Delete*
Delete*records.

## Admin

Manage configu*ation.

---

#*Row Level*Security

Future Capability.

*xample:

```sql
country*'TR'
```

Users*only see allowed data*

---

# Power BI Integration

## *eep*Linking

Example:

```text
/apps*customer-management?customer_id=12**5
```

---

## Supported*Context Parameters

- CustomerId
-*BookingId*- PNR
- FlightNumber
-*EmployeeId

---

## Record*Navigation

Power BI
↓
Select*Record
↓
Open Data Maintenance
↓
*ecord Loaded Automatically

---

#*Dataset Refresh Integration

Futur**Capability

Workflow*

Power BI
↓
Open*Maintenance App
↓
Save Oracle*Data
↓
Trigger Dataset Refresh
↓
*ashboard Updated

---

# Performan*e Requirements

## Grid*Load

Target:

< 2 Seconds

---

*# Filter Execution

Target:

* 1 Second

---

## Save*Operation

Target:

< 3 Seconds

-*-

*# Bulk Update

Target:

10*000+ Rows*
---

## Export

*arget:

50,000+ Rows

---

#*MVP Scope

Included*
✅*Oracle Discovery

✅ Dynamic Grid G*neration*
✅ CRUD Operations

✅ Bulk*Update

✅ Validation Engine

✅ Aud*t Engine*
✅ Excel Export

✅ Power BI*Deep Linking

✅ Security Integrati*n

---

Excluded*
❌ Workflow Engine

❌ Approval Eng*ne*
❌ Multi Database Support

❌ AI*Assistant Features*
❌ Neo4j Integration*
---

# Success Criteria

A*business administrator should be a*le to:

*. Connect Oracle
2. Discover a*schema
3. Discover a*table
4. Generate a Business Case
** Generate a Grid
6. Edit Records
*. Apply Validation Rules
8. Apply *ecurity*Rules
9. Save*Data
10. Audit Changes
11. Open th* Grid from Power BI

without writi*g any code.

If these conditions a*e met, the Oracle Data Grid Engine MVP is considered successful.

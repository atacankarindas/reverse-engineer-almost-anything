# Frontend Specification

## Objective

Build a modern web frontend for a metadata-driven data management platform inspired by Apparo Fast Edit.

The application should allow administrators and business users to create, configure and operate data-centric applications without custom UI development.

The platform should generate user experiences dynamically from metadata rather than hardcoded page implementations.

Reference model: product_specification.md, navigation_map.md, agent_build_spec.md. 【1-581c9f】【2-9b59b0】【3-996567】

---

# Technology Stack

## Core Framework

- React
- TypeScript
- Vite

## UI Framework

- Material UI (MUI)

## State Management

- TanStack Query
- Zustand

## Routing

- React Router

## Forms

- React Hook Form
- Zod

## Data Grids

- AG Grid Community

## Authentication

- Microsoft Entra ID (Azure AD)

---

# Design Principles

## Metadata Driven

Screens should be generated from metadata.

Avoid hardcoded forms wherever possible.

Example:

BusinessCase Metadata
↓
Form Definition
↓
Dynamic Renderer
↓
Generated UI

---

## Configuration First

Users configure applications.

Developers build platform capabilities.

Business logic should live in metadata rather than frontend code.

---

## Enterprise Focus

Frontend must support:

- Large datasets
- Authorization
- Auditing
- Administration
- Multi-user environments

---

# Layout Structure

```text
┌─────────────────────────────────────┐
│ Top Toolbar                         │
├─────────────┬───────────────────────┤
│ Sidebar     │ Main Content Area     │
│ Navigation  │                       │
│             │                       │
├─────────────┴───────────────────────┤
│ Notification Area                   │
└─────────────────────────────────────┘
```

---

# Application Areas

## Dashboard

Purpose:

Landing page for all platform activities.

Features:

- Recent Business Cases
- Favorites
- Recently Modified
- System Notifications
- Quick Actions

---

## Business Case Management

Route:

```text
/business-cases
```

Features:

- Search
- Filter
- Create
- Edit
- Duplicate
- Delete
- Archive

View:

```text
Grid View
```

Columns:

- Name
- Description
- Status
- Owner
- Last Modified

Actions:

- Open
- Edit
- Clone
- Delete

---

## Business Case Designer

Route:

```text
/business-cases/:id/designer
```

Purpose:

Configure metadata for business applications.

Sections:

- General Settings
- Data Source
- Widgets
- Security
- Validation
- Workflow
- Import/Export

Navigation Style:

Tabbed Layout

---

## Widget Designer

Route:

```text
/business-cases/:id/widgets
```

Purpose:

Create and manage widgets.

Supported Widget Types:

### Input Controls

- Textbox
- Text Area
- Numeric Input
- Date Picker
- Checkbox
- Dropdown
- Radio Group

### Display Components

- Label
- Badge
- Status Indicator

### Grid Components

- Data Grid
- Readonly Grid
- Tree Grid

Features:

- Drag & Drop Ordering
- Property Editor
- Validation Assignment
- Visibility Rules

---

## Data Maintenance

Route:

```text
/apps/:businessCaseId
```

Purpose:

Provide data entry interface.

Views:

### Form View

Single Record Editing

### Grid View

Bulk Operations

Capabilities:

- Insert
- Update
- Delete
- Copy
- Bulk Update
- Search
- Filter
- Export

---

## Connection Management

Route:

```text
/connections
```

Purpose:

Manage Oracle connections.

Features:

- Create Connection
- Edit Connection
- Test Connection
- Discover Objects

Supported First Release:

- Oracle Database

Future Releases:

- PostgreSQL
- SQL Server

---

## Security Administration

Route:

```text
/security
```

Features:

- User Management
- Role Management
- Permission Assignment
- Security Groups

Views:

- User List
- Role List
- Group List

---

## Workflow Management

Route:

```text
/workflows
```

Purpose:

Manage process definitions.

Features:

- Create Workflow
- Modify Workflow
- Assign Workflow
- Activate Workflow

---

# Dynamic Engine Components

## Dynamic Form Renderer

Input:

```json
{
  "fields": []
}
```

Output:

Generated Form

Responsibilities:

- Render controls
- Run validations
- Manage state

---

## Dynamic Grid Renderer

Input:

```json
{
  "columns": []
}
```

Output:

Generated Grid

Capabilities:

- Sorting
- Filtering
- Paging
- Inline Editing

---

## Validation Renderer

Input:

Validation Metadata

Capabilities:

- Required
- Min Length
- Max Length
- Regex
- Custom Rule

---

## Security Renderer

Input:

Permission Metadata

Capabilities:

- Hide
- Disable
- Readonly
- Full Access

---

# Power BI Integration

## Goal

Provide data maintenance capabilities alongside Power BI reporting.

The platform should complement Power BI rather than replace it.

---

## Integration Patterns

### Launch From Power BI

Power BI
↓
Deep Link
↓
Business Case

Example:

```text
/apps/customer?id=12345
```

---

### Context Transfer

Power BI visual
↓
Selected Record
↓
Open Maintenance Screen

Example:

```text
Customer ID
Booking ID
Flight Number
```

passed through URL parameters.

---

### Refresh Friendly Design

Expected Flow:

Power BI
↓
Open Record
↓
Edit Data
↓
Save
↓
Trigger Dataset Refresh

---

# Navigation Hierarchy

```text
Dashboard

├── Business Cases
│
├── Applications
│
├── Workflows
│
├── Security
│
├── Connections
│
└── Administration
```

Reference: navigation_map.md. 【2-9b59b0】

---

# User Experience Requirements

## Administrators

Must be able to:

- Configure metadata
- Configure security
- Configure workflows

---

## Data Operators

Must be able to:

- Search data
- Edit data
- Validate data
- Export data

---

## Managers

Must be able to:

- Monitor workflows
- Review audit history
- Review exceptions

---

# Responsive Requirements

Desktop First

Supported Widths:

- 1920px
- 1600px
- 1440px
- 1366px

Minimum:

- 1280px

Mobile support is not required in first release.

---

# Accessibility

Minimum Compliance:

- WCAG 2.1 AA

Requirements:

- Keyboard Navigation
- Screen Reader Compatibility
- High Contrast Support

---

# Build Priority

Phase 1

- Authentication
- Navigation
- Business Cases

Phase 2

- Widget Designer
- Dynamic Forms

Phase 3

- Data Grid Engine
- Oracle Integration

Phase 4

- Security
- Workflow Engine

Phase 5

- Power BI Integration
- Audit History
- Advanced Administration

---

# Frontend Success Criteria

The platform should allow a business administrator to:

1. Create a Business Case
2. Configure Widgets
3. Connect to Oracle
4. Generate a Data Entry Screen
5. Edit Data
6. Apply Security
7. Use the application without writing code

When these steps are possible, the frontend MVP is considered complete.

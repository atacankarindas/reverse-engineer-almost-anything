# Product Specification

## Product Name

Apparo Fast Edit

---

# Product Overview

Apparo Fast Edit is a low-code data management platform integrated with QlikView.

The platform enables business users and administrators to build, configure and maintain data-entry applications without developing custom software.

Applications are created through configurable Business Cases, Widgets, Workflows, Security Rules and Data Connections.

The platform appears to focus on:

- Data maintenance
- Workflow configuration
- Security management
- Metadata-driven application development
- Excel based data exchange
- Qlik integration

---

# Product Goals

The product aims to:

1. Reduce software development effort for business applications.
2. Enable configurable data-entry solutions.
3. Provide secure access to data.
4. Allow non-developers to manage application behavior.
5. Integrate with existing enterprise data sources.

---

# Core Concepts

## Business Case

The primary object in the system.

A Business Case represents a configurable business application.

Examples:

- Product Maintenance
- Pricing Entry
- Forecast Entry
- Master Data Management

A Business Case contains:

- Widgets
- Security Settings
- Validation Rules
- Data Source Configuration
- Workflow Configuration

---

## Widget

Widgets are configurable UI elements.

Examples:

- Text Fields
- Checkboxes
- Dropdowns
- Date Pickers
- Grid Columns
- Labels

Widgets are used to build user-facing screens.

---

## Connection

Represents a connection to an external database.

Connection properties include:

- Database Type
- Host
- Port
- Schema
- Authentication Settings

---

## Security Group

Represents authorization boundaries.

Security Groups determine:

- Who can access a Business Case
- Who can edit data
- Who can view data
- Widget-level visibility

---

## Workflow

Represents configurable business processes.

Workflows may control:

- Validation
- Approval
- User actions
- Automated processing

---

# User Roles

## System Administrator

Responsibilities:

- System configuration
- Connection management
- Security management

---

## Business Administrator

Responsibilities:

- Create and maintain Business Cases
- Configure workflows
- Configure validations

---

## Designer

Responsibilities:

- Design widgets
- Configure user experiences
- Manage screen layouts

---

## Data User

Responsibilities:

- Create records
- Update records
- Delete records
- Import and export data

---

# Functional Modules

## Dashboard

Provides access to all core product functionality.

Capabilities:

- Navigation
- Application access
- Administrative access

---

## Business Case Management

Capabilities:

- Create Business Case
- Edit Business Case
- Copy Business Case
- Delete Business Case
- Organize Business Cases

---

## Business Case Designer

Capabilities:

- Configure application behavior
- Configure validations
- Configure permissions
- Configure workflows
- Configure actions

---

## Widget Designer

Capabilities:

- Create Widget
- Edit Widget
- Delete Widget
- Configure Widget Behavior

Supported Components:

- Text Input
- Number Input
- Checkbox
- Dropdown
- Date Selector
- Labels
- Grid Columns

---

## Data Management

Capabilities:

- Insert Records
- Update Records
- Delete Records
- Bulk Update
- Search
- Filter
- Refresh

---

## Import Export

Capabilities:

- Excel Import
- Excel Export
- CSV Import
- CSV Export

---

## Security Administration

Capabilities:

- Create Security Groups
- Assign Permissions
- Configure Read Only Access
- Restrict Widget Visibility

---

## Connection Management

Capabilities:

- Create Database Connections
- Test Connections
- Update Connections
- Remove Connections

Supported Database Types:

- Oracle
- SQL Server
- PostgreSQL

---

# Navigation Model

Dashboard

→ Business Cases

→ Business Case Designer

→ Widgets

→ Data Management

→ Security

→ Connections

→ Administration

---

# Data Management Features

The platform supports editable grid operations.

Supported operations:

- Insert Row
- Update Row
- Delete Row
- Bulk Update
- Refresh Data

Additional Features:

- Data Validation
- Audit Tracking
- History Tracking

---

# Security Model

The platform uses group-based authorization.

Security can be configured at:

- Business Case Level
- Widget Level
- User Level

Supported access modes:

- Read Only
- Edit
- Full Administration

---

# Integration Points

## Database Integration

Used to connect business applications to enterprise databases.

Configuration includes:

- Host
- Port
- Schema
- Authentication

---

## Qlik Integration

Observed integrations:

- QlikView
- Qlik Security
- Qlik Reporting

The platform appears to act as a configurable editing layer on top of Qlik-based reporting environments.

---

# Domain Model

Client
│
├── Business Cases
│
├── Users
│
└── Connections

Business Case
│
├── Widgets
├── Workflow Definitions
├── Validation Rules
├── Permissions
└── Data Sources

Widget
│
├── Display Configuration
├── Validation Configuration
└── Security Configuration

Security Group
│
├── Users
├── Business Cases
└── Widgets

---

# Rebuild Considerations

When rebuilding this product:

1. Use metadata-driven architecture.
2. Keep Business Case as the central domain object.
3. Implement configurable Widget definitions.
4. Support role-based authorization.
5. Support dynamic forms.
6. Support dynamic grids.
7. Support import/export workflows.
8. Keep workflow configuration separated from business data.

The rebuilt platform should function as a low-code data management framework rather than a set of hardcoded business applications.

# Agent Build Specification

## Objective

Rebuild a modern web-based version of Apparo Fast Edit.

The rebuilt application should preserve the observed functionality, workflows and user experience patterns while using a modern technology stack.

The goal is functional equivalence, not pixel-perfect cloning.

---

# Product Summary

Apparo Fast Edit appears to be a low-code data management platform.

The platform allows users to:

- Configure business applications
- Manage database-backed forms
- Configure widgets
- Configure workflows
- Define security and permissions
- Import and export data
- Maintain data through editable grids

The primary configuration object is called a Business Case.

A Business Case acts as a container for:

- Widgets
- Data sources
- Validation rules
- Security settings
- Workflow settings

---

# Recommended Architecture

## Frontend

Technology:

- React
- TypeScript
- Material UI

Key Requirements:

- Responsive layout
- Sidebar navigation
- Configuration pages
- Data grids
- Forms
- Administration panels

---

## Backend

Technology:

- FastAPI

Responsibilities:

- Authentication
- Authorization
- Configuration management
- Metadata management
- Workflow execution
- Import/Export operations

---

## Database

Technology:

- PostgreSQL

Purpose:

- Store application metadata
- Store workflows
- Store widget definitions
- Store security settings
- Store connection definitions

---

# Domain Model

## Client

Represents a tenant or customer.

Properties:

- id
- name
- description
- status

---

## BusinessCase

Represents a configurable application.

Properties:

- id
- name
- description
- status
- connection_id

Relationships:

- contains widgets
- contains workflows
- contains validations
- contains permissions

---

## Widget

Represents a UI component.

Properties:

- id
- name
- widget_type
- label
- sort_order

Relationships:

- belongs to business case

---

## Workflow

Represents a business process.

Properties:

- id
- name
- description
- status

Relationships:

- belongs to business case

---

## Connection

Represents a database connection.

Properties:

- id
- name
- database_type
- host
- port
- schema_name

---

## SecurityGroup

Represents authorization groups.

Properties:

- id
- name
- description

Relationships:

- assigned to widgets
- assigned to business cases

---

## ValidationRule

Represents data validation logic.

Properties:

- id
- name
- expression
- error_message

---

# Application Modules

---

## Module 1

Business Case Management

Purpose:

Manage configurable data applications.

Pages:

- Business Case List
- Create Business Case
- Edit Business Case
- Clone Business Case
- Delete Business Case

Capabilities:

- Search
- Filter
- Create
- Edit
- Copy
- Delete

---

## Module 2

Business Case Designer

Purpose:

Configure behavior of a Business Case.

Pages:

- Main Settings
- Standard Buttons
- Custom Buttons
- Data Filters
- Validation Settings
- Audit Settings
- Security Settings

Capabilities:

- Enable features
- Configure permissions
- Configure workflows
- Configure validations

---

## Module 3

Widget Designer

Purpose:

Manage screen widgets.

Pages:

- Widget List
- Widget Management
- Widget Properties

Capabilities:

- Create widget
- Edit widget
- Delete widget
- Reorder widget

Supported Widget Types:

- Text Input
- Numeric Input
- Dropdown
- Checkbox
- Date Picker
- Label
- Table Grid

---

## Module 4

Data Management

Purpose:

Maintain business data.

Pages:

- Data Entry Grid
- Data History
- Audit History

Capabilities:

- Insert
- Update
- Delete
- Copy
- Bulk Update
- Refresh

---

## Module 5

Connection Management

Purpose:

Manage database connections.

Pages:

- Connection List
- Create Connection
- Edit Connection
- Connection Test

Capabilities:

- Create connection
- Validate connection
- Modify connection

Supported Databases:

- PostgreSQL
- Oracle
- SQL Server

---

## Module 6

Security Administration

Purpose:

Manage permissions.

Pages:

- Security Groups
- User Permissions
- Widget Permissions
- Business Case Permissions

Capabilities:

- Assign permissions
- Revoke permissions
- Configure readonly access

---

## Module 7

Import Export

Purpose:

Exchange data with external tools.

Capabilities:

- Excel Import
- Excel Export
- CSV Import
- CSV Export

---

# Navigation Tree

Dashboard

├── Business Cases

│   ├── List

│   ├── Create

│   ├── Edit

│   └── Clone

│

├── Business Case Designer

│   ├── Main Settings

│   ├── Widgets

│   ├── Security

│   ├── Validation

│   └── Workflow

│

├── Connections

│

├── Security

│

└── Administration

---

# User Stories

## Business Administrator

As a business administrator,

I want to create a Business Case,

So that I can configure a new editable application.

Acceptance Criteria:

- Business Case can be created
- Business Case can be modified
- Business Case can be deleted

---

## Designer

As a designer,

I want to add widgets,

So that users can enter and edit data.

Acceptance Criteria:

- Widget creation supported
- Widget editing supported
- Widget ordering supported

---

## Security Administrator

As a security administrator,

I want to assign permissions,

So that users only access authorized features.

Acceptance Criteria:

- Group-based permission assignment
- Read-only mode support

---

## Data User

As a data user,

I want to edit records,

So that business data can be maintained.

Acceptance Criteria:

- Create record
- Update record
- Delete record
- Bulk update record

---

# UI Components

Required Components:

- Application Layout
- Left Navigation Menu
- Top Toolbar
- Business Case Grid
- Widget Grid
- Connection Grid
- Security Grid
- Dynamic Forms
- Configuration Panels
- Audit Panels
- Import Export Dialogs

---

# Non Functional Requirements

Performance:

- Page load < 2 seconds
- Grid rendering < 1 second for 1,000 rows

Security:

- Role-based authorization
- Audit logging
- Session management

Maintainability:

- Modular architecture
- Type-safe frontend
- API-first backend

---

# Build Order

Phase 1

- Authentication
- Business Case Management
- Basic Navigation

Phase 2

- Widget Designer
- Dynamic Forms
- CRUD Operations

Phase 3

- Permissions
- Validation Engine
- Workflow Configuration

Phase 4

- Excel Import Export
- Audit History
- Advanced Administration

---

# Instructions For Coding Agent

Build the application incrementally.

Start with:

1. PostgreSQL schema
2. FastAPI backend
3. React frontend shell
4. Business Case module
5. Widget module

After the core metadata model is completed, implement:

- Dynamic forms
- Authorization
- Import/Export
- Workflow engine

Focus on configuration-driven architecture rather than hardcoded business logic.

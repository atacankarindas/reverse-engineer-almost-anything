# REA Context

## Objective

Reconstruct a modern equivalent of Apparo Fast Edit based on tutorial video analysis.

The goal is functional equivalence, not pixel-perfect UI recreation.

This document consolidates all discovered information from:

- Screen analysis
- Product specification
- Navigation analysis
- Application blueprint

---

# Confidence Levels

## High Confidence

Information repeatedly observed in application screens.

## Medium Confidence

Information inferred from multiple screens but not explicitly confirmed.

## Low Confidence

Reasonable assumptions used only for reconstruction planning.

---

# High Confidence Findings

## Product Name

Apparo Fast Edit

---

## Core Concepts

The following concepts appear repeatedly throughout the application:

- Business Case
- Widget
- Connection
- Security Group
- Validation
- Workflow
- Client
- Data Import
- Data Export
- Audit History
- Qlik Integration

---

## Primary Object

Business Case

The Business Case appears to be the central configuration object in the platform.

Observed relationships:

Business Case
    ├── Widgets
    ├── Validation Rules
    ├── Security Settings
    ├── Workflow Settings
    └── Data Configuration

---

## Widget System

Widgets are configurable UI elements.

Observed capabilities:

- Create Widget
- Edit Widget
- Delete Widget
- Configure Widget Properties

Observed widget categories:

- Text Input
- Numeric Input
- Dropdown
- Checkbox
- Grid Components
- Labels

---

## Security System

Observed capabilities:

- Security Groups
- Permissions
- Read Only Access
- Widget Access Restrictions
- Business Case Access Restrictions

---

## Connection Management

Observed configuration areas:

- Database Type
- Host
- Port
- Schema
- Authentication Settings

The application can connect to external data sources.

---

## Data Management

Observed operations:

- Insert Record
- Update Record
- Delete Record
- Copy Record
- Bulk Update
- Refresh Data

Observed supporting features:

- Validation
- Audit History
- Filtering

---

## Import Export

Observed capabilities:

- Excel Import
- Excel Export

Additional formats are not confirmed.

---

# Medium Confidence Findings

## Product Category

The application appears to be a low-code metadata-driven platform.

Evidence:

- Extensive configuration screens
- Widget management
- Workflow configuration
- Security configuration
- Dynamic data management

---

## Application Architecture

The application appears to follow:

Business Case
    ↓
Metadata Configuration
    ↓
Generated Forms
    ↓
Data Management Screens

rather than hardcoded application pages.

---

## Workflow Engine

Workflow configuration screens were observed.

The exact workflow execution model was not visible.

Assume configurable workflow behavior exists.

Do not assume approval processes unless additional evidence is found.

---

## Qlik Integration

Observed references:

- QlikView
- Qlik Security
- Qlik Reporting

The product appears to function as a configurable editing layer integrated with the Qlik ecosystem.

---

# Unknown Areas

The following could not be determined from the analyzed videos:

- Backend technology stack
- Actual database schema
- Internal service architecture
- API structure
- Deployment topology
- Authentication mechanism
- Workflow engine implementation

Do not assume these details reflect the original product.

---

# Reconstructed Domain Model

Client
│
├── Business Cases
├── Users
└── Connections

BusinessCase
│
├── Widgets
├── Validation Rules
├── Security Rules
├── Workflow Definitions
└── Data Sources

Widget
│
├── UI Definition
├── Validation Configuration
├── Display Configuration
└── Security Configuration

SecurityGroup
│
├── Users
├── Business Cases
└── Widgets

Connection
│
├── Database Type
├── Host
├── Port
├── Schema
└── Credentials

---

# Reconstructed Navigation

Dashboard

├── Business Cases
│   ├── Create
│   ├── Edit
│   ├── Copy
│   └── Delete
│
├── Business Case Designer
│   ├── Main Settings
│   ├── Widgets
│   ├── Validation
│   ├── Security
│   └── Workflow
│
├── Data Management
│
├── Connections
│
├── Security
│
└── Administration

This structure contains observed and inferred navigation paths.

Treat it as a reconstruction rather than an exact copy.

---

# Functional Requirements

## Business Case Management

The platform shall allow:

- Creating Business Cases
- Editing Business Cases
- Copying Business Cases
- Deleting Business Cases

---

## Widget Management

The platform shall allow:

- Creating widgets
- Editing widgets
- Deleting widgets
- Configuring widget properties

---

## Data Management

The platform shall allow:

- Creating records
- Updating records
- Deleting records
- Bulk editing records

---

## Security

The platform shall support:

- Security groups
- Permission assignment
- Read-only access
- Business Case permissions
- Widget permissions

---

## Integration

The platform shall support:

- External database connections
- Configurable data sources
- Excel import
- Excel export

---

# Recommended Modern Implementation

This section represents reconstruction choices and not observed facts.

Frontend:

- React
- TypeScript
- Material UI

Backend:

- FastAPI

Database:

- PostgreSQL

Optional:

- Neo4j for metadata relationships

---

# Critical Design Principle

The rebuilt application MUST be metadata-driven.

Do not hardcode:

- Forms
- Data Grids
- Workflows
- Permissions

Instead implement:

Business Case
    ↓
Metadata
    ↓
Dynamic UI Generation

The metadata model is the core product capability.

This principle is more important than matching the visual appearance of the original application.

---

# Instructions For REA

Treat the analyzed software as:

A metadata-driven low-code platform for creating configurable business applications.

Prioritize:

1. Metadata Model
2. Business Case Engine
3. Widget Engine
4. Dynamic Form Rendering
5. Dynamic Grid Rendering
6. Security Engine
7. Workflow Engine
8. Import / Export Features

Do not optimize for visual similarity.

Optimize for behavioral similarity and architectural flexibility.

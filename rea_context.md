# REA Context

## Objective

Reconstruct a modern metadata-driven data maintenance platform inspired by concepts discovered in Apparo Fast Edit tutorial videos.

The goal is not to clone the original product.

The goal is to rebuild the underlying ideas using a modern Microsoft-centric architecture built around:

- Oracle Database
- Microsoft Power BI
- Microsoft Entra ID

The rebuilt platform should provide secure, governed and scalable data maintenance capabilities for enterprise analytics environments.

---

# Confidence Model

This document separates information into three categories.

## High Confidence

Information directly observed in analyzed screens.

## Medium Confidence

Information inferred from multiple observed screens.

## Reconstruction Recommendations

Design decisions intentionally introduced to modernize the platform.

---

# Source Product Heritage

## Observed Product

Apparo Fast Edit

Observed references:

- QlikView
- Qlik Security
- Qlik Reporting

These observations belong to the original product.

The rebuilt platform should not be considered a Qlik solution.

Instead, the platform should apply the same metadata-driven concepts within a Microsoft ecosystem architecture.

---

# Target Platform

The reconstructed platform targets:

## Data Platform

- Oracle Database

## Analytics Platform

- Microsoft Power BI

## Identity Platform

- Microsoft Entra ID

## Core Objective

Provide a governed data maintenance layer that complements Power BI reporting and Oracle-based enterprise data platforms.

Power BI remains the reporting and analytics system.

The rebuilt application provides:

- Data maintenance
- Data correction
- Dynamic forms
- Dynamic grids
- Security management
- Metadata management
- Workflow configuration

---

# Product Positioning

Think of the rebuilt platform as:

Power BI
+
Oracle
+
Metadata Driven Data Maintenance

rather than:

Qlik
+
Data Editing

---

# Problem Statement

Organizations frequently identify data quality issues through reporting and analytics tools.

Business users can identify problems in Power BI dashboards but often lack a governed mechanism for correcting source data.

A typical process looks like:

Power BI
↓
Issue Identified
↓
Email / Excel
↓
Manual Process
↓
Data Team
↓
Database Update
↓
Refresh Dashboard

The rebuilt platform aims to simplify this workflow.

Target process:

Power BI
↓
Issue Identified
↓
Open Maintenance Screen
↓
Update Oracle Data
↓
Save
↓
Audit Created
↓
Dataset Refreshed
↓
Dashboard Updated

---

# High Confidence Findings

## Core Concepts

The following concepts appeared repeatedly throughout analyzed screens:

- Business Case
- Widget
- Connection
- Security Group
- Validation
- Workflow
- Client
- Audit History
- Data Import
- Data Export

These concepts form the core domain of the platform.

---

## Business Case

Confidence: High

Business Case appears to be the primary configuration object within the system.

Observed relationships:

Business Case
├── Widgets
├── Validation Rules
├── Security Settings
├── Workflow Settings
└── Data Source Configuration

Business Cases appear to represent configurable business applications.

---

## Widget System

Confidence: High

Widgets are configurable UI elements used to build user experiences.

Observed capabilities:

- Create Widget
- Edit Widget
- Delete Widget
- Configure Widget

Observed widget categories:

- Text Input
- Numeric Input
- Dropdown
- Checkbox
- Grid Components
- Labels

---

## Connection Management

Confidence: High

The platform includes dedicated connection management capabilities.

Observed configuration areas:

- Database Type
- Host
- Port
- Schema
- Connection Settings

External database integration is a core capability.

---

## Security

Confidence: High

Observed capabilities:

- Security Groups
- User Permissions
- Read Only Access
- Widget Permissions
- Business Case Permissions

Security appears to operate at multiple layers.

---

## Data Management

Confidence: High

Observed capabilities:

- Insert Records
- Update Records
- Delete Records
- Copy Records
- Bulk Updates
- Refresh Data

Observed supporting features:

- Validation
- Audit History
- Filtering

---

## Import / Export

Confidence: High

Observed capabilities:

- Excel Import
- Excel Export

Support for additional formats was not clearly confirmed.

---

# Medium Confidence Findings

## Product Category

The platform appears to function as a metadata-driven low-code application builder.

Evidence includes:

- Extensive configuration interfaces
- Widget management
- Workflow configuration
- Security configuration
- Dynamic data management

---

## Architecture Style

The platform appears to follow a configuration-first architecture.

Observed pattern:

Business Case
↓
Metadata
↓
Generated Forms
↓
Generated Data Screens

The platform appears to generate behavior from configuration rather than hardcoded application logic.

---

## Workflow Engine

Workflow configuration capabilities were observed.

However, the execution model remains unknown.

Assume workflow definitions exist.

Do not assume approval workflows unless explicitly discovered later.

---

# Unknown Areas

The following information could not be determined from video analysis:

- Backend technology stack
- Actual database schema
- API architecture
- Deployment architecture
- Authentication implementation
- Workflow engine implementation
- Notification engine
- Scheduling capabilities

These should not be treated as facts.

---

# Oracle First Strategy

The first product release should support Oracle only.

Rationale:

- Reduced complexity
- Faster MVP delivery
- Better metadata discovery
- Enterprise compatibility
- Alignment with existing Oracle-centric environments

---

## Oracle Discovery Capabilities

The system should automatically discover:

### Schemas

Using:

- ALL_USERS

### Tables

Using:

- ALL_TABLES

### Views

Using:

- ALL_VIEWS

### Columns

Using:

- ALL_TAB_COLUMNS

### Primary Keys

Using:

- ALL_CONSTRAINTS
- ALL_CONS_COLUMNS

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
├── Workflow Definitions
├── Security Rules
└── Data Sources

Widget
│
├── Display Configuration
├── Validation Configuration
├── Security Configuration
└── Rendering Rules

Connection
│
├── Database Type
├── Host
├── Port
├── Schema
└── Authentication Settings

SecurityGroup
│
├── Users
├── Widgets
└── Business Cases

---

# Reconstructed Navigation

Dashboard

├── Business Cases
│   ├── Create
│   ├── Edit
│   ├── Clone
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

This structure combines observed and inferred navigation paths.

Treat it as guidance rather than an exact reproduction.

---

# Oracle Data Grid Concept

## Purpose

Provide configurable maintenance screens on top of Oracle tables and views.

---

## Supported Source Types

### Oracle Table

CRUD enabled.

Example:

CUSTOMER_MASTER

---

### Oracle View

Read-only by default.

Update support can be enabled if Oracle update mechanisms exist.

---

### Custom Query

Metadata-defined query sources.

Used for advanced business cases.

---

## Grid Capabilities

### Read

Dynamic querying.

### Insert

Create new records.

### Update

Modify existing records.

### Delete

Remove records.

### Bulk Update

Update multiple records simultaneously.

### Export

Excel export support.

---

## Validation Support

Metadata-driven validation rules:

- Required
- Length Constraints
- Numeric Limits
- Pattern Matching
- Custom Rules

---

## Audit Support

Every modification should generate audit records.

Track:

- User
- Timestamp
- Table
- Field
- Old Value
- New Value

---

# Power BI Integration Strategy

## Objective

Make Power BI the primary discovery experience and the rebuilt product the primary maintenance experience.

---

## Deep Linking

Power BI should be able to launch the application with context.

Example:

```text
/apps/customer-maintenance?customer_id=12345
```

---

## Context Passing

Supported context attributes:

- CustomerId
- BookingId
- PNR
- FlightNumber
- EmployeeId

---

## Data Correction Journey

Power BI Dashboard
↓
User Identifies Issue
↓
Open Maintenance Screen
↓
Edit Oracle Record
↓
Validate Changes
↓
Save
↓
Audit Created
↓
Optional Dataset Refresh
↓
Updated Power BI Dashboard

This user journey represents the primary business value of the rebuilt platform.

---

# Functional Requirements

## Business Case Management

The platform shall allow:

- Create Business Case
- Edit Business Case
- Copy Business Case
- Delete Business Case

---

## Widget Management

The platform shall allow:

- Create Widgets
- Modify Widgets
- Delete Widgets
- Configure Widget Properties

---

## Data Management

The platform shall allow:

- Record Creation
- Record Update
- Record Deletion
- Bulk Update
- Filtering
- Searching

---

## Security

The platform shall support:

- Security Groups
- Permission Assignment
- Read-only Access
- Widget Permissions
- Business Case Permissions

---

## Oracle Integration

The platform shall support:

- Schema Discovery
- Table Discovery
- View Discovery
- Primary Key Discovery
- Dynamic CRUD Operations

---

## Power BI Integration

The platform shall support:

- Deep Linking
- Context Passing
- Record-Level Navigation
- Power BI Driven Data Maintenance

---

# Recommended Modern Implementation

This section contains implementation recommendations and not observed facts.

Frontend:

- React
- TypeScript
- Material UI

Backend:

- FastAPI

Metadata Store:

- PostgreSQL

Business Data:

- Oracle Database

Identity:

- Microsoft Entra ID

Optional:

- Neo4j for metadata relationship analysis

---

# Critical Design Principle

The platform must remain metadata-driven.

Do not hardcode:

- Forms
- Data Grids
- Business Applications
- Workflow Definitions
- Permission Models

Instead:

Business Case
↓
Metadata
↓
Generated Forms
↓
Generated Grids
↓
Generated User Experience

The metadata engine is the core product capability.

---

# Instructions For REA

Treat the analyzed software as inspiration rather than a product to clone.

Build a modern Oracle + Power BI platform based on the discovered concepts.

Prioritize implementation in the following order:

1. Oracle Discovery Engine
2. Business Case Engine
3. Dynamic Grid Engine
4. Dynamic Form Engine
5. Security Engine
6. Power BI Deep Linking
7. Audit Engine
8. Workflow Engine

Do not optimize for visual similarity.

Optimize for:

- Metadata-driven architecture
- Enterprise scalability
- Oracle operability
- Power BI integration
- Maintainability
- Extensibility

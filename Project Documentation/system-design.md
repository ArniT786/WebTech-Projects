# System Design

## Overview

AgriFlowTrack follows a three-tier web application architecture.

---

## Architecture Layers

### 1. Presentation Layer

Responsible for user interaction.

Technologies:

* HTML5
* CSS3
* JavaScript

Functions:

* User Interface
* Dashboard
* Forms
* Reports

---

### 2. Business Logic Layer

Responsible for processing user requests.

Technologies:

* PHP

Functions:

* Authentication
* Inventory Processing
* FEFO Logic
* Report Generation

---

### 3. Data Layer

Responsible for data storage and retrieval.

Technologies:

* MySQL
* phpMyAdmin

Functions:

* Data Storage
* Data Retrieval
* Backup Management

---

## System Modules

### User Management Module

* Registration
* Login
* Role Management

### Crop Management Module

* Crop Records
* Sowing Management

### Harvest Management Module

* Harvest Tracking
* Quantity Monitoring

### Packaging Module

* Batch Management
* Packaging Tracking

### Inventory Module

* Stock Monitoring
* Warehouse Tracking

### Storage Monitoring Module

* Temperature Records
* Humidity Records

### Reporting Module

* Inventory Reports
* Warehouse Reports
* Expiration Reports

---

## Security Design

* Password Hashing
* Role-Based Access Control
* Session Management
* Database Access Control

# Technical Design Document (TDD)

## Project Name

AgriFlowTrack

---

## Technology Stack

### Frontend

* HTML5
* CSS3
* JavaScript
* Bootstrap

### Backend

* PHP 8+

### Database

* MySQL

### Server

* Apache Server

### Development Environment

* XAMPP

---

## Folder Structure

/project-root

/assets

/css

/js

/images

/config

/database

/modules

/users

/crops

/harvests

/inventory

/warehouse

/reports

/includes

index.php

login.php

dashboard.php

---

## Design Principles

### Modularity

Each module is independently managed.

### Scalability

Future IoT and AI integration supported.

### Security

User authentication and authorization enforced.

### Maintainability

Reusable code structure.

---

## Core Components

### Authentication Component

Handles:

* Login
* Logout
* Session Validation

### Inventory Component

Handles:

* Stock Tracking
* Product Movement

### Warehouse Component

Handles:

* Storage Monitoring
* Capacity Management

### Reporting Component

Handles:

* Report Generation
* Data Export

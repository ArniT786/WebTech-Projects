# Software Requirements Specification (SRS)

## 1. Introduction

### 1.1 Purpose

This Software Requirements Specification (SRS) document defines the functional and non-functional requirements of the AgriFlowTrack system.

### 1.2 Scope

AgriFlowTrack is a web-based agricultural inventory management platform designed to support farmers, processors, and warehouse managers through centralized inventory tracking, storage monitoring, and FEFO-based management.

---

## 2. Overall Description

### Product Perspective

The system provides a centralized platform for:

* Crop Management
* Harvest Management
* Packaging Management
* Inventory Management
* Storage Monitoring

### Product Users

* Farmers
* Processors
* Warehouse Managers
* Administrators

---

## 3. Functional Requirements

The system shall:

* Authenticate users.
* Manage crops.
* Manage harvest records.
* Track inventory.
* Monitor warehouses.
* Manage packaging.
* Track shelf life.
* Generate reports.
* Support FEFO inventory management.

---

## 4. Non-Functional Requirements

The system shall:

* Load pages within 3 seconds.
* Maintain 99.5% uptime.
* Support secure authentication.
* Support role-based access control.
* Maintain data integrity.
* Support future scalability.

---

## 5. System Architecture

### Frontend

* HTML
* CSS
* JavaScript

### Backend

* PHP

### Database

* MySQL

### Database Management

* phpMyAdmin

---

## 6. Data Requirements

Main data entities:

* User
* Crop
* Crop Sowing
* Harvest
* Warehouse
* Sensor Data
* Packaged Batch
* Packaged Product
* Delivery

---

## 7. Constraints

* Internet connection required.
* Initial system uses manual data entry.
* Limited real-time IoT integration.

---

## 8. Assumptions

* Users provide accurate information.
* Warehouses maintain storage records.
* Administrators manage access properly.

---

## 9. Future Scope

* AI-based recommendations
* IoT integration
* Mobile application
* Predictive analytics
* Smart inventory forecasting

---

## 10. Conclusion

AgriFlowTrack provides a centralized agricultural inventory management solution that supports production tracking, inventory monitoring, packaging management, warehouse control, and FEFO-based perishable product handling. The system is expected to reduce agricultural losses, improve decision-making, and enhance supply chain efficiency.

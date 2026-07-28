# Entity Relationship Diagram (ERD)

## Overview

The AgriFlowTrack database is designed to manage agricultural production, harvesting, packaging, storage, inventory, and delivery information.

---

ERD diagram: ![alt text](<erd pic-1.png>)
<img width="1408" height="768" alt="erd pic" src="https://github.com/user-attachments/assets/4f0f2c40-0a72-4b4a-ae01-a59408365b39" />


## Entities

### User

| Attribute    | Type     |
| ------------ | -------- |
| user_id (PK) | INT      |
| name         | VARCHAR  |
| email        | VARCHAR  |
| password     | VARCHAR  |
| role         | ENUM     |
| created_at   | DATETIME |

---

### Farm

| Attribute      | Type    |
| -------------- | ------- |
| farm_id (PK)   | INT     |
| farmer_id (FK) | INT     |
| farm_name      | VARCHAR |
| location       | VARCHAR |
| area_size      | DECIMAL |

---

### Crop

| Attribute       | Type    |
| --------------- | ------- |
| crop_id (PK)    | INT     |
| crop_name       | VARCHAR |
| category        | VARCHAR |
| shelf_life_days | INT     |

---

### Crop_Sowing

| Attribute      | Type    |
| -------------- | ------- |
| sowing_id (PK) | INT     |
| crop_id (FK)   | INT     |
| farm_id (FK)   | INT     |
| sowing_date    | DATE    |
| seed_quantity  | DECIMAL |

---

### Harvest

| Attribute       | Type    |
| --------------- | ------- |
| harvest_id (PK) | INT     |
| sowing_id (FK)  | INT     |
| harvest_date    | DATE    |
| quantity        | DECIMAL |

---

### Warehouse

| Attribute         | Type    |
| ----------------- | ------- |
| warehouse_id (PK) | INT     |
| warehouse_name    | VARCHAR |
| location          | VARCHAR |
| capacity          | DECIMAL |

---

### Sensor_Data

| Attribute         | Type     |
| ----------------- | -------- |
| sensor_id (PK)    | INT      |
| warehouse_id (FK) | INT      |
| temperature       | DECIMAL  |
| humidity          | DECIMAL  |
| recorded_at       | DATETIME |

---

### Packaged_Batch

| Attribute       | Type    |
| --------------- | ------- |
| batch_id (PK)   | INT     |
| harvest_id (FK) | INT     |
| packaging_date  | DATE    |
| batch_code      | VARCHAR |

---

### Packaged_Product

| Attribute       | Type    |
| --------------- | ------- |
| product_id (PK) | INT     |
| batch_id (FK)   | INT     |
| quantity        | DECIMAL |
| expiry_date     | DATE    |

---

### Delivery

| Attribute        | Type    |
| ---------------- | ------- |
| delivery_id (PK) | INT     |
| product_id (FK)  | INT     |
| destination      | VARCHAR |
| delivery_date    | DATE    |

---

## Relationships

Farm 1 ----- N Crop_Sowing

Crop 1 ----- N Crop_Sowing

Crop_Sowing 1 ----- N Harvest

Harvest 1 ----- N Packaged_Batch

Packaged_Batch 1 ----- N Packaged_Product

Warehouse 1 ----- N Sensor_Data

Packaged_Product 1 ----- N Delivery

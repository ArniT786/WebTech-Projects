# API Design

## Overview

AgriFlowTrack uses RESTful APIs for communication between frontend and backend systems.

Base URL:

```http
/api/v1
```

---

# Authentication APIs

## Login

```http
POST /auth/login
```

### Request

```json
{
  "email": "user@example.com",
  "password": "password123"
}
```

### Response

```json
{
  "status": true,
  "token": "jwt_token"
}
```

---

## Logout

```http
POST /auth/logout
```

---

# Crop APIs

## Get All Crops

```http
GET /crops
```

---

## Add Crop

```http
POST /crops
```

### Request

```json
{
  "crop_name": "Tomato",
  "category": "Vegetable",
  "shelf_life_days": 15
}
```

---

## Update Crop

```http
PUT /crops/{id}
```

---

## Delete Crop

```http
DELETE /crops/{id}
```

---

# Harvest APIs

## Add Harvest

```http
POST /harvests
```

---

## Get Harvests

```http
GET /harvests
```

---

# Inventory APIs

## Get Inventory

```http
GET /inventory
```

---

## Update Inventory

```http
PUT /inventory/{id}
```

---

# Warehouse APIs

## Get Warehouses

```http
GET /warehouses
```

---

## Add Warehouse

```http
POST /warehouses
```

---

# Sensor APIs

## Add Sensor Data

```http
POST /sensor-data
```

### Request

```json
{
  "warehouse_id": 1,
  "temperature": 8.5,
  "humidity": 70
}
```

---

# Reports APIs

## Inventory Report

```http
GET /reports/inventory
```

---

## Expiration Report

```http
GET /reports/expiration
```

---

## Warehouse Report

```http
GET /reports/warehouse
```

---

## API Security

* JWT Authentication
* HTTPS Communication
* Role-Based Authorization
* Input Validation
* SQL Injection Protection

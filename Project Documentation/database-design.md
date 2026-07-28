# Database Design

## Database Name

agriflowtrack_db

---

## Users Table

```sql
users
```

| Field      | Type         |
| ---------- | ------------ |
| user_id    | INT PK       |
| name       | VARCHAR(100) |
| email      | VARCHAR(100) |
| password   | VARCHAR(255) |
| role       | ENUM         |
| created_at | DATETIME     |

---

## Crops Table

```sql
crops
```

| Field           | Type         |
| --------------- | ------------ |
| crop_id         | INT PK       |
| crop_name       | VARCHAR(100) |
| category        | VARCHAR(50)  |
| shelf_life_days | INT          |

---

## Farms Table

```sql
farms
```

| Field     | Type         |
| --------- | ------------ |
| farm_id   | INT PK       |
| farmer_id | INT FK       |
| farm_name | VARCHAR(100) |
| location  | VARCHAR(255) |

---

## Crop_Sowing Table

```sql
crop_sowing
```

| Field         | Type    |
| ------------- | ------- |
| sowing_id     | INT PK  |
| crop_id       | INT FK  |
| farm_id       | INT FK  |
| sowing_date   | DATE    |
| seed_quantity | DECIMAL |

---

## Harvest Table

```sql
harvests
```

| Field        | Type    |
| ------------ | ------- |
| harvest_id   | INT PK  |
| sowing_id    | INT FK  |
| quantity     | DECIMAL |
| harvest_date | DATE    |

---

## Warehouse Table

```sql
warehouses
```

| Field          | Type         |
| -------------- | ------------ |
| warehouse_id   | INT PK       |
| warehouse_name | VARCHAR(100) |
| location       | VARCHAR(255) |
| capacity       | DECIMAL      |

---

## Sensor_Data Table

```sql
sensor_data
```

| Field        | Type     |
| ------------ | -------- |
| sensor_id    | INT PK   |
| warehouse_id | INT FK   |
| temperature  | DECIMAL  |
| humidity     | DECIMAL  |
| recorded_at  | DATETIME |

---

## Packaged_Batch Table

```sql
packaged_batches
```

| Field          | Type        |
| -------------- | ----------- |
| batch_id       | INT PK      |
| harvest_id     | INT FK      |
| packaging_date | DATE        |
| batch_code     | VARCHAR(50) |

---

## Packaged_Product Table

```sql
packaged_products
```

| Field       | Type    |
| ----------- | ------- |
| product_id  | INT PK  |
| batch_id    | INT FK  |
| quantity    | DECIMAL |
| expiry_date | DATE    |

---

## Delivery Table

```sql
deliveries
```

| Field         | Type         |
| ------------- | ------------ |
| delivery_id   | INT PK       |
| product_id    | INT FK       |
| destination   | VARCHAR(255) |
| delivery_date | DATE         |

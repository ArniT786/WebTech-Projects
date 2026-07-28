# Use Cases

## Actors

* Farmer
* Processor
* Warehouse Manager
* Administrator

---

# UC-01 Login

### Actor

All Users

### Description

User logs into the system.

### Preconditions

User account exists.

### Main Flow

1. User enters credentials.
2. System validates credentials.
3. System grants access.

### Postconditions

User dashboard is displayed.

---

# UC-02 Add Crop

### Actor

Farmer

### Description

Farmer registers a crop.

### Preconditions

Farmer is logged in.

### Main Flow

1. Open Crop Module.
2. Enter crop information.
3. Save record.

### Postconditions

Crop data stored successfully.

---

# UC-03 Record Harvest

### Actor

Farmer

### Description

Record harvested crop information.

### Main Flow

1. Select crop.
2. Enter harvest details.
3. Save information.

### Postconditions

Harvest record created.

---

# UC-04 Create Package Batch

### Actor

Processor

### Description

Create packaging batch.

### Main Flow

1. Select harvested product.
2. Enter packaging information.
3. Generate batch.

### Postconditions

Batch created.

---

# UC-05 Monitor Inventory

### Actor

Warehouse Manager

### Description

View inventory information.

### Main Flow

1. Open inventory module.
2. View stock records.
3. Monitor storage status.

### Postconditions

Inventory status displayed.

---

# UC-06 FEFO Management

### Actor

Warehouse Manager

### Description

Manage products using FEFO.

### Main Flow

1. View expiration dates.
2. Sort products.
3. Prioritize earliest-expiring products.

### Postconditions

Inventory ordered by FEFO rules.

---

# UC-07 Generate Reports

### Actor

Administrator

### Description

Generate system reports.

### Main Flow

1. Select report type.
2. Generate report.
3. Download report.

### Postconditions

Report generated successfully.

# Acceptance Criteria

## Agricultural Product Management

### AC-01: Crop Registration

**Given**
A farmer is logged into the system.

**When**
The farmer enters crop details and clicks Save.

**Then**
The crop information shall be stored successfully in the database.

---

### AC-02: Harvest Recording

**Given**
A crop record exists.

**When**
The farmer submits harvest information.

**Then**
The harvest record shall be linked to the crop.

---

## Inventory Management

### AC-03: Inventory Update

**Given**
A new harvest has been recorded.

**When**
Inventory is updated.

**Then**
The stock quantity shall reflect the updated value.

---

### AC-04: Warehouse Tracking

**Given**
A product is stored in a warehouse.

**When**
The warehouse manager views inventory.

**Then**
Storage location information shall be displayed.

---

## Packaging Management

### AC-05: Batch Creation

**Given**
A processor is logged in.

**When**
A new batch is created.

**Then**
The system shall generate a unique batch identifier.

---

### AC-06: Packaging Information

**Given**
A packaged product exists.

**When**
Packaging details are submitted.

**Then**
The information shall be stored successfully.

---

## Perishable Product Management

### AC-07: Shelf-Life Monitoring

**Given**
A product has an expiration date.

**When**
The manager views product details.

**Then**
The remaining shelf life shall be displayed.

---

### AC-08: FEFO Recommendation

**Given**
Multiple batches exist.

**When**
The inventory report is generated.

**Then**
Products with the earliest expiration dates shall be prioritized.

---

### AC-09: Expiration Alert

**Given**
A product is approaching expiration.

**When**
The threshold period is reached.

**Then**
The system shall generate an alert notification.

---

## Security

### AC-10: User Authentication

**Given**
A user enters valid credentials.

**When**
The Login button is clicked.

**Then**
Access shall be granted.

---

### AC-11: Unauthorized Access

**Given**
A user attempts restricted access.

**When**
Permission is unavailable.

**Then**
Access shall be denied.

---

## Reporting

### AC-12: Inventory Report Generation

**Given**
Inventory data exists.

**When**
A report is requested.

**Then**
The system shall generate an accurate inventory report.

---

## Performance

### AC-13: Dashboard Loading

**Given**
The user is logged in.

**When**
The dashboard is opened.

**Then**
The page shall load within 3 seconds.

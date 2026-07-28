# Data Flow Diagram (DFD)

## DFD Level 0 (Context Diagram)

### External Entities

1. Farmer
2. Processor
3. Warehouse Manager
4. Administrator

### Main Process

AgriFlowTrack Inventory Management System

### Data Flows

Farmer → Crop Data → System

Processor → Packaging Data → System

Warehouse Manager → Storage Data → System

Administrator → User Management Data → System

System → Reports → Users

---

## DFD Level 1

### Process 1.0 User Management

Input:

* Login Data
* User Information

Output:

* User Access
* Authentication Result

Data Store:

* User Database

---

### Process 2.0 Crop Management

Input:

* Crop Information
* Sowing Data

Output:

* Crop Records

Data Store:

* Crop Database

---

### Process 3.0 Harvest Management

Input:

* Harvest Data

Output:

* Harvest Records

Data Store:

* Harvest Database

---

### Process 4.0 Packaging Management

Input:

* Packaging Information

Output:

* Batch Information

Data Store:

* Package Database

---

### Process 5.0 Inventory Management

Input:

* Product Information

Output:

* Inventory Status

Data Store:

* Inventory Database

---

### Process 6.0 Warehouse Monitoring

Input:

* Temperature Data
* Humidity Data

Output:

* Storage Reports

Data Store:

* Sensor Data Database

---

### Process 7.0 Reporting

Input:

* System Data

Output:

* Reports
* Analytics

Data Store:

* All Databases

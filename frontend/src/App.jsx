import React, { useState, useEffect } from 'react';
import Login from './components/Login';
import Sidebar from './components/Sidebar';
import Dashboard from './components/Dashboard';
import CrudPage from './components/CrudPage';

export default function App() {
  const [isLoggedIn, setIsLoggedIn] = useState(false);
  const [username, setUsername] = useState('');
  const [activeTab, setActiveTab] = useState('dashboard');

  // Verify auth on mount
  useEffect(() => {
    const auth = localStorage.getItem('agriflow_auth');
    const user = localStorage.getItem('agriflow_username');
    if (auth === 'true' && user) {
      setIsLoggedIn(true);
      setUsername(user);
    }
  }, []);

  const handleLoginSuccess = (user) => {
    setIsLoggedIn(true);
    setUsername(user);
  };

  const handleLogout = () => {
    localStorage.removeItem('agriflow_auth');
    localStorage.removeItem('agriflow_username');
    setIsLoggedIn(false);
    setUsername('');
    setActiveTab('dashboard');
  };

  // If not logged in, render the login page
  if (!isLoggedIn) {
    return <Login onLoginSuccess={handleLoginSuccess} />;
  }

  // Configuration for 9 CRUD screens
  const crudConfigs = {
    agricultural_products: {
      title: "Agricultural Products",
      endpoint: "agricultural_products",
      columns: ['ID', 'Product Name', 'Category', 'Growing Date', 'Harvest Date', 'Storage Requirements', 'Shelf Life', 'Packaging Details'],
      columnKeys: ['id', 'product_name', 'category', 'growing_date', 'harvest_date', 'storage_requirements', 'shelf_life', 'packaging_details'],
      fields: [
        { name: 'product_name', label: 'Product Name', type: 'text', placeholder: 'e.g. Fresh Tomato (Local)', required: true },
        { name: 'category', label: 'Category', type: 'text', placeholder: 'e.g. Vegetable / Fruit / Grain', required: true },
        { name: 'growing_date', label: 'Growing Date', type: 'date', required: false },
        { name: 'harvest_date', label: 'Harvest Date', type: 'date', required: false },
        { name: 'storage_requirements', label: 'Storage Requirements', type: 'text', placeholder: 'e.g. Cold Storage at 5°C', required: false },
        { name: 'shelf_life', label: 'Shelf Life', type: 'text', placeholder: 'e.g. 7 days', required: false },
        { name: 'packaging_details', label: 'Packaging Details', type: 'text', placeholder: 'e.g. Carton boxes', required: false },
      ]
    },
    agri_inputs: {
      title: "Agri Inputs",
      endpoint: "agri_inputs",
      columns: ['ID', 'Item', 'Quantity', 'Unit', 'Date Received', 'Input Type', 'Name', 'Stock Level', 'Usage Rate/Week', 'Procurement Date'],
      columnKeys: ['id', 'item', 'quantity', 'unit', 'date_received', 'input_type', 'name', 'stock_level', 'usage_rate_per_week', 'procurement_date'],
      fields: [
        { name: 'item', label: 'Item Type', type: 'text', placeholder: 'e.g. Urea', required: true },
        { name: 'name', label: 'Item Name / Spec', type: 'text', placeholder: 'e.g. Urea 46%', required: true },
        { name: 'quantity', label: 'Quantity', type: 'number', placeholder: 'e.g. 100.00', required: true },
        { name: 'unit', label: 'Unit', type: 'text', placeholder: 'e.g. bags / liters', required: true },
        { name: 'input_type', label: 'Category', type: 'text', placeholder: 'e.g. Fertilizer / Pesticide', required: false },
        { name: 'stock_level', label: 'Stock Level', type: 'text', placeholder: 'e.g. High / Medium / Low', required: false },
        { name: 'usage_rate_per_week', label: 'Usage / Week', type: 'text', placeholder: 'e.g. 10.00', required: false },
        { name: 'date_received', label: 'Date Received', type: 'date', required: false },
        { name: 'procurement_date', label: 'Procurement Date', type: 'date', required: false },
      ]
    },
    perishable_products: {
      title: "Perishable Products",
      endpoint: "perishable_products",
      columns: ['ID', 'Name', 'Batch Number', 'Storage Temp', 'Shelf Life (days)', 'Status', 'Added Date'],
      columnKeys: ['id', 'name', 'batch_number', 'storage_temp', 'shelf_life_days', 'status', 'added_date'],
      fields: [
        { name: 'name', label: 'Product Name', type: 'text', placeholder: 'e.g. Fresh Mangoes', required: true },
        { name: 'batch_number', label: 'Batch Number', type: 'text', placeholder: 'e.g. BATCH-2025-09', required: false },
        { name: 'storage_temp', label: 'Storage Temperature', type: 'text', placeholder: 'e.g. 4°C', required: false },
        { name: 'shelf_life_days', label: 'Shelf Life (Days)', type: 'number', placeholder: 'e.g. 10', required: false },
        { name: 'status', label: 'Status', type: 'text', placeholder: 'e.g. Fresh / Expired / Near Expiry', required: false },
        { name: 'added_date', label: 'Added Date', type: 'date', required: false },
      ]
    },
    post_harvest_monitor: {
      title: "Post-Harvest Monitor",
      endpoint: "post_harvest_monitor",
      columns: ['ID', 'Crop Name', 'Moisture Level', 'Temperature', 'Visual Inspection', 'Inspection Date', 'Inspector'],
      columnKeys: ['id', 'crop_name', 'moisture_level', 'temperature', 'visual_inspection', 'inspection_date', 'inspector'],
      fields: [
        { name: 'crop_name', label: 'Crop Name', type: 'text', placeholder: 'e.g. Wheat', required: true },
        { name: 'moisture_level', label: 'Moisture Level', type: 'text', placeholder: 'e.g. 12%', required: false },
        { name: 'temperature', label: 'Temperature', type: 'text', placeholder: 'e.g. 24°C', required: false },
        { name: 'visual_inspection', label: 'Visual Inspection Notes', type: 'text', placeholder: 'e.g. Healthy grains, no insects', required: false },
        { name: 'inspector', label: 'Inspector Name', type: 'text', placeholder: 'e.g. John Doe', required: false },
        { name: 'inspection_date', label: 'Inspection Date', type: 'date', required: false },
      ]
    },
    storage_conditions: {
      title: "Storage Conditions",
      endpoint: "storage_conditions",
      columns: ['ID', 'Facility Name', 'Current Temp', 'Humidity', 'Ventilation Status', 'Last Checked'],
      columnKeys: ['id', 'facility_name', 'current_temp', 'humidity', 'ventilation_status', 'last_checked'],
      fields: [
        { name: 'facility_name', label: 'Facility / Room Name', type: 'text', placeholder: 'e.g. Warehouse Cold Unit A', required: true },
        { name: 'current_temp', label: 'Current Temperature', type: 'text', placeholder: 'e.g. 5°C', required: false },
        { name: 'humidity', label: 'Humidity Level', type: 'text', placeholder: 'e.g. 85%', required: false },
        { name: 'ventilation_status', label: 'Ventilation Status', type: 'text', placeholder: 'e.g. Active / Inactive', required: false },
        { name: 'last_checked', label: 'Last Checked Date', type: 'date', required: false },
      ]
    },
    harvested_crops: {
      title: "Harvested Crops",
      endpoint: "harvested_crops",
      columns: ['ID', 'Name', 'Quantity', 'Storage Condition', 'Movement Details', 'Expiry Date'],
      columnKeys: ['id', 'name', 'quantity', 'storage_condition', 'movement_details', 'expiry_date'],
      fields: [
        { name: 'name', label: 'Crop Name', type: 'text', placeholder: 'e.g. Wheat', required: true },
        { name: 'quantity', label: 'Quantity', type: 'number', placeholder: 'e.g. 1500.00', required: true },
        { name: 'storage_condition', label: 'Storage Condition', type: 'text', placeholder: 'e.g. Dry Storage', required: false },
        { name: 'expiry_date', label: 'Expiry Date', type: 'date', required: false },
        { name: 'movement_details', label: 'Movement Details', type: 'textarea', placeholder: 'e.g. Transferred from Farm Field A to Silo 2', required: false },
      ]
    },
    tracking_of_products: {
      title: "Tracking of Products",
      endpoint: "tracking_of_products",
      columns: ['ID', 'Product Name', 'Current Location', 'Destination', 'Transit Status', 'Dispatch Date'],
      columnKeys: ['id', 'product_name', 'current_location', 'destination', 'transit_status', 'dispatch_date'],
      fields: [
        { name: 'product_name', label: 'Product Name', type: 'text', placeholder: 'e.g. Maize Grains', required: true },
        { name: 'current_location', label: 'Current Location', type: 'text', placeholder: 'e.g. Warehouse 1', required: false },
        { name: 'destination', label: 'Destination', type: 'text', placeholder: 'e.g. Mombasa Central Market', required: false },
        { name: 'transit_status', label: 'Transit Status', type: 'text', placeholder: 'e.g. Dispatched / In Transit / Arrived', required: false },
        { name: 'dispatch_date', label: 'Dispatch Date', type: 'date', required: false },
      ]
    },
    market_data: {
      title: "Market Data",
      endpoint: "market_data",
      columns: ['ID', 'Market', 'Product', 'Price / Unit', 'Date'],
      columnKeys: ['id', 'market', 'product', 'price_per_unit', 'date'],
      fields: [
        { name: 'market', label: 'Market Location', type: 'text', placeholder: 'e.g. Nairobi Wakulima', required: true },
        { name: 'product', label: 'Product Name', type: 'text', placeholder: 'e.g. Maize / Tomato', required: true },
        { name: 'price_per_unit', label: 'Price Per Unit', type: 'number', placeholder: 'e.g. 1.30', required: true },
        { name: 'date', label: 'Date Reported', type: 'date', required: false },
      ]
    },
    inventory: {
      title: "Inventory",
      endpoint: "inventory",
      columns: ['ID', 'Item Name', 'Amount', 'Unit', 'Date Entered', 'Expiry Date', 'Destination', 'Warehouse', 'Notes'],
      columnKeys: ['id', 'item_name', 'amount', 'unit', 'date_entered', 'expiry_date', 'destination', 'warehouse', 'notes'],
      fields: [
        { name: 'item_name', label: 'Item Name', type: 'text', placeholder: 'e.g. Urea Fertilizer', required: true },
        { name: 'amount', label: 'Amount', type: 'number', placeholder: 'e.g. 100.00', required: true },
        { name: 'unit', label: 'Unit', type: 'text', placeholder: 'e.g. bags / kg', required: true },
        { name: 'destination', label: 'Destination', type: 'text', placeholder: 'e.g. Field B', required: false },
        { name: 'warehouse', label: 'Warehouse Room', type: 'text', placeholder: 'e.g. Warehouse A', required: false },
        { name: 'date_entered', label: 'Date Entered', type: 'date', required: false },
        { name: 'expiry_date', label: 'Expiry Date', type: 'date', required: false },
        { name: 'notes', label: 'Notes', type: 'textarea', placeholder: 'Any specific instructions, quality issues, or context...', required: false },
      ]
    }
  };

  return (
    <div id="root" style={{ display: 'flex', width: '100vw', height: '100vh' }}>
      <Sidebar 
        activeTab={activeTab} 
        setActiveTab={setActiveTab} 
        onLogout={handleLogout} 
      />
      
      <main className="main-content">
        {activeTab === 'dashboard' ? (
          <Dashboard />
        ) : (
          <CrudPage 
            key={activeTab} // Using key triggers remount with clean state for new endpoints
            title={crudConfigs[activeTab].title}
            endpoint={crudConfigs[activeTab].endpoint}
            fields={crudConfigs[activeTab].fields}
            columns={crudConfigs[activeTab].columns}
            columnKeys={crudConfigs[activeTab].columnKeys}
          />
        )}
      </main>
    </div>
  );
}

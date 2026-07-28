import React from 'react';

export default function Sidebar({ activeTab, setActiveTab, onLogout }) {
  const menuItems = [
    { id: 'dashboard', label: 'Dashboard' },
    { id: 'agricultural_products', label: 'Agricultural Products' },
    { id: 'agri_inputs', label: 'Agri Inputs' },
    { id: 'perishable_products', label: 'Perishable Products' },
    { id: 'post_harvest_monitor', label: 'Post-Harvest Monitor' },
    { id: 'storage_conditions', label: 'Storage Conditions' },
    { id: 'harvested_crops', label: 'Harvested Crops' },
    { id: 'tracking_of_products', label: 'Tracking of Products' },
    { id: 'market_data', label: 'Market Data' },
    { id: 'inventory', label: 'Inventory' },
  ];

  return (
    <aside className="sidebar">
      <div className="sidebar-header">
        <h2>AgriFlowTrack</h2>
      </div>
      <ul className="nav-links">
        {menuItems.map((item) => (
          <li
            key={item.id}
            className={`nav-item ${activeTab === item.id ? 'active' : ''}`}
            onClick={() => setActiveTab(item.id)}
          >
            {item.label}
          </li>
        ))}
      </ul>
      <div className="logout-container">
        <button className="logout-btn" onClick={onLogout}>
          Logout
        </button>
      </div>
    </aside>
  );
}

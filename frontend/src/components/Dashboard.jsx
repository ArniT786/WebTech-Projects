import React, { useState, useEffect } from 'react';

export default function Dashboard() {
  const [data, setData] = useState(null);
  const [loading, setLoading] = useState(true);
  const [error, setError] = useState('');

  const fetchDashboardData = async () => {
    setLoading(true);
    setError('');
    try {
      const response = await fetch('http://localhost:8000/api/dashboard');
      if (!response.ok) throw new Error('Failed to load dashboard data');
      const result = await response.json();
      setData(result);
    } catch (err) {
      console.error(err);
      setError('Could not connect to the API server.');
    } finally {
      setLoading(false);
    }
  };

  useEffect(() => {
    fetchDashboardData();
  }, []);

  if (loading && !data) {
    return (
      <div style={{ display: 'flex', justifyContent: 'center', alignItems: 'center', height: '60vh' }}>
        <p style={{ color: 'var(--text-secondary)', fontSize: '1.1rem' }}>Loading dashboard summary...</p>
      </div>
    );
  }

  if (error) {
    return (
      <div style={{ padding: '20px', background: 'rgba(239,68,68,0.1)', border: '1px solid rgba(239,68,68,0.2)', borderRadius: '12px', color: '#ef4444' }}>
        <p>{error}</p>
        <button className="btn btn-primary" onClick={fetchDashboardData} style={{ marginTop: '10px' }}>Retry</button>
      </div>
    );
  }

  return (
    <>
      <div className="header-row">
        <h1>Dashboard</h1>
        <div className="header-actions">
          <button className="btn btn-refresh" onClick={fetchDashboardData}>
            Refresh
          </button>
        </div>
      </div>

      <div className="summary-grid">
        <div className="summary-card">
          <h3>{data?.productsCount ?? 0}</h3>
          <p>Products</p>
        </div>
        <div className="summary-card">
          <h3>{data?.agriInputsCount ?? 0}</h3>
          <p>Agri Inputs</p>
        </div>
        <div className="summary-card">
          <h3>{data?.perishablesCount ?? 0}</h3>
          <p>Perishables</p>
        </div>
        <div className="summary-card">
          <h3>{data?.postHarvestCount ?? 0}</h3>
          <p>Post-Harvest</p>
        </div>
      </div>

      <div className="card">
        <h2 className="card-title">Latest Market Prices</h2>
        <div className="table-responsive">
          <table>
            <thead>
              <tr>
                <th>Market</th>
                <th>Product</th>
                <th>Price / Unit</th>
                <th>Date</th>
              </tr>
            </thead>
            <tbody>
              {data?.marketData && data.marketData.length > 0 ? (
                data.marketData.map((row) => (
                  <tr key={row.id}>
                    <td>{row.market}</td>
                    <td>{row.product}</td>
                    <td>{row.price_per_unit != null ? `$${parseFloat(row.price_per_unit).toFixed(2)}` : '-'}</td>
                    <td>{row.date || '-'}</td>
                  </tr>
                ))
              ) : (
                <tr>
                  <td colSpan="4" style={{ textAlign: 'center' }}>No market data records found</td>
                </tr>
              )}
            </tbody>
          </table>
        </div>
      </div>
    </>
  );
}

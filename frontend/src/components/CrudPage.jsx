import React, { useState, useEffect } from 'react';

export default function CrudPage({ title, endpoint, fields, columns, columnKeys }) {
  const [data, setData] = useState([]);
  const [loading, setLoading] = useState(false);
  const [error, setError] = useState('');
  const [successMsg, setSuccessMsg] = useState('');
  const [searchQuery, setSearchQuery] = useState('');
  
  // Form state
  const [formValues, setFormValues] = useState({});
  const [editId, setEditId] = useState(null);

  // Initialize empty form values
  useEffect(() => {
    resetForm();
    loadData();
  }, [endpoint]);

  const resetForm = () => {
    const initialValues = {};
    fields.forEach(f => {
      initialValues[f.name] = '';
    });
    setFormValues(initialValues);
    setEditId(null);
  };

  const loadData = async () => {
    setLoading(true);
    setError('');
    try {
      const response = await fetch(`http://localhost:8000/api/${endpoint}`);
      if (!response.ok) throw new Error(`HTTP error! status: ${response.status}`);
      const result = await response.json();
      setData(result);
    } catch (err) {
      console.error(err);
      setError(`Failed to load data for ${title}.`);
    } finally {
      setLoading(false);
    }
  };

  const showToast = (message, isSuccess = true) => {
    if (isSuccess) {
      setSuccessMsg(message);
      setTimeout(() => setSuccessMsg(''), 3000);
    } else {
      setError(message);
      setTimeout(() => setError(''), 4000);
    }
  };

  const handleInputChange = (name, value) => {
    setFormValues(prev => ({
      ...prev,
      [name]: value
    }));
  };

  const handleSubmit = async (e) => {
    e.preventDefault();
    setError('');

    // Prepare body
    const bodyData = { ...formValues };
    if (editId) {
      bodyData.id = editId;
    }

    // Number conversion for required float/integer fields
    fields.forEach(f => {
      if (f.type === 'number') {
        if (bodyData[f.name] === '') {
          bodyData[f.name] = null;
        } else {
          bodyData[f.name] = Number(bodyData[f.name]);
        }
      }
    });

    const method = editId ? 'PUT' : 'POST';

    try {
      const response = await fetch(`http://localhost:8000/api/${endpoint}`, {
        method: method,
        headers: {
          'Content-Type': 'application/json'
        },
        body: JSON.stringify(bodyData)
      });

      const result = await response.json();

      if (response.ok) {
        showToast(result.message || 'Record saved successfully.');
        resetForm();
        loadData();
      } else {
        showToast(result.detail || 'Failed to save record.', false);
      }
    } catch (err) {
      console.error(err);
      showToast('Connection to server failed.', false);
    }
  };

  const handleEdit = (row) => {
    const editValues = {};
    fields.forEach(f => {
      editValues[f.name] = row[f.name] != null ? row[f.name] : '';
    });
    setFormValues(editValues);
    setEditId(row.id);
    
    // Smooth scroll to form
    const formElement = document.getElementById('data-form-card');
    if (formElement) {
      formElement.scrollIntoView({ behavior: 'smooth' });
    }
  };

  const handleDelete = async (id) => {
    if (!window.confirm('Are you sure you want to delete this record?')) return;

    try {
      const response = await fetch(`http://localhost:8000/api/${endpoint}`, {
        method: 'DELETE',
        headers: {
          'Content-Type': 'application/json'
        },
        body: JSON.stringify({ id })
      });

      const result = await response.json();

      if (response.ok) {
        showToast(result.message || 'Record deleted.');
        loadData();
        if (editId === id) {
          resetForm();
        }
      } else {
        showToast(result.detail || 'Deletion failed.', false);
      }
    } catch (err) {
      console.error(err);
      showToast('Connection to server failed.', false);
    }
  };

  // Client-side search filtering
  const filteredData = data.filter(row => {
    if (!searchQuery) return true;
    const filter = searchQuery.toLowerCase();
    return columnKeys.some(key => {
      const val = row[key];
      if (val == null) return false;
      return String(val).toLowerCase().includes(filter);
    }) || String(row.id).includes(filter);
  });

  return (
    <>
      {successMsg && <div className="alert-popup success">{successMsg}</div>}
      {error && <div className="alert-popup error">{error}</div>}

      <div className="header-row">
        <h1>{title}</h1>
        <div className="header-actions">
          <input
            type="text"
            className="search-input"
            placeholder="Search in table..."
            value={searchQuery}
            onChange={(e) => setSearchQuery(e.target.value)}
          />
          <button className="btn btn-refresh" onClick={loadData} disabled={loading}>
            {loading ? 'Refreshing...' : 'Refresh'}
          </button>
        </div>
      </div>

      <div className="card" id="data-form-card">
        <h2 className="card-title">{editId ? `Edit Record (ID: ${editId})` : 'Create / Edit'}</h2>
        <form onSubmit={handleSubmit}>
          {/* We group fields in pairs of form-grids for nice layout, or form-grid-full for textareas */}
          <div className="form-grid">
            {fields.filter(f => f.type !== 'textarea').map(f => (
              <div className="form-group" key={f.name}>
                <label htmlFor={f.name}>{f.label}</label>
                <input
                  type={f.type}
                  id={f.name}
                  name={f.name}
                  placeholder={f.placeholder}
                  value={formValues[f.name] || ''}
                  onChange={(e) => handleInputChange(f.name, e.target.value)}
                  required={f.required}
                  step={f.type === 'number' ? 'any' : undefined}
                />
              </div>
            ))}
          </div>

          {fields.filter(f => f.type === 'textarea').map(f => (
            <div className="form-grid form-grid-full" key={f.name} style={{ marginTop: '15px' }}>
              <div className="form-group">
                <label htmlFor={f.name}>{f.label}</label>
                <textarea
                  id={f.name}
                  name={f.name}
                  placeholder={f.placeholder}
                  value={formValues[f.name] || ''}
                  onChange={(e) => handleInputChange(f.name, e.target.value)}
                  required={f.required}
                  rows={3}
                />
              </div>
            </div>
          ))}

          <div className="form-actions" style={{ marginTop: '20px' }}>
            <button type="submit" className="btn btn-primary">
              {editId ? 'Update' : 'Save'}
            </button>
            <button type="button" className="btn btn-secondary" onClick={resetForm}>
              Reset
            </button>
          </div>
        </form>
      </div>

      <div className="card">
        <div className="table-responsive">
          <table>
            <thead>
              <tr>
                {columns.map((col, idx) => (
                  <th key={idx}>{col}</th>
                ))}
                <th>Actions</th>
              </tr>
            </thead>
            <tbody>
              {filteredData.length > 0 ? (
                filteredData.map((row) => (
                  <tr key={row.id}>
                    {columnKeys.map((key, idx) => (
                      <td key={idx}>{row[key] != null ? String(row[key]) : '-'}</td>
                    ))}
                    <td className="action-buttons">
                      <button className="btn btn-sm btn-secondary" onClick={() => handleEdit(row)}>
                        Edit
                      </button>
                      <button className="btn btn-sm btn-danger" onClick={() => handleDelete(row.id)}>
                        Delete
                      </button>
                    </td>
                  </tr>
                ))
              ) : (
                <tr>
                  <td colSpan={columns.length + 1} style={{ textAlign: 'center' }}>
                    {loading ? 'Loading records...' : 'No records found'}
                  </td>
                </tr>
              )}
            </tbody>
          </table>
        </div>
      </div>
    </>
  );
}

# AgriFlowTrack

A modern rebuild of the AgriFlowTrack Agricultural DBMS project. The frontend is built using **React** (Vite), and the backend is built using **FastAPI** (Python). 

The project connects to a SQLite database (`agriflow.db`) by default and automatically seeds the initial database tables and sample records.

---

## Folder Structure

- `/backend`: FastAPI Python source code, SQLAlchemy database models, and requirements.
- `/frontend`: React SPA source code using Vite.

---

## How to Run

### 1. Run the Backend (FastAPI)

1. Open a terminal and navigate to the `backend` directory:
   ```bash
   cd backend
   ```
2. Activate the virtual environment:
   - **On Windows (PowerShell):**
     ```powershell
     .\venv\Scripts\Activate.ps1
     ```
   - **On macOS/Linux:**
     ```bash
     source venv/bin/activate
     ```
3. (Optional) If you ever add new packages, install them via:
   ```bash
   pip install -r requirements.txt
   ```
4. Start the FastAPI server using `uvicorn`:
   ```bash
   uvicorn main:app --reload
   ```
   The backend server will run on [http://localhost:8000](http://localhost:8000). You can view the automated API documentation at [http://localhost:8000/docs](http://localhost:8000/docs).

---

### 2. Run the Frontend (React)

1. Open another terminal and navigate to the `frontend` directory:
   ```bash
   cd frontend
   ```
2. Install npm packages (already pre-installed in this workspace):
   ```bash
   npm install
   ```
3. Start the Vite React development server:
   ```bash
   npm run dev
   ```
   The frontend application will run on [http://localhost:5173](http://localhost:5173).

---

## Authentication Credentials

To log into the system, use the default administrator credentials:
- **Username:** `admin`
- **Password:** `admin123`

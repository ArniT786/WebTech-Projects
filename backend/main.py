from fastapi import FastAPI, Depends, HTTPException, status
from fastapi.middleware.cors import CORSMiddleware
from sqlalchemy.orm import Session
from datetime import date
from typing import List, Optional
from pydantic import BaseModel

from database import engine, Base, get_db
import models, schemas

# Initialize FastAPI application
app = FastAPI(title="AgriFlowTrack API", version="1.0.0")

# Add CORS Middleware to allow React frontend to connect
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # For production, restrict to React origin
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

class DeleteRequest(BaseModel):
    id: int

# Initialize Database and Seed Data
@app.on_event("startup")
def startup_db_setup():
    # Create all tables if they don't exist
    Base.metadata.create_all(bind=engine)
    
    # Seed initial data if tables are empty
    db = next(get_db())
    try:
        # 1. Seed Admin User
        if db.query(models.AdminUser).count() == 0:
            admin = models.AdminUser(username="admin", password="admin123")
            db.add(admin)
            db.commit()

        # 2. Seed Agricultural Products
        if db.query(models.AgriculturalProduct).count() == 0:
            prod1 = models.AgriculturalProduct(
                product_name="Tomato",
                category="Vegetable",
                growing_date=date(2025, 7, 10),
                harvest_date=date(2025, 8, 15),
                storage_requirements="Cold Storage at 5°C",
                shelf_life="7 days",
                packaging_details="Carton boxes"
            )
            prod2 = models.AgriculturalProduct(
                product_name="Maize",
                category="Grain",
                growing_date=date(2025, 5, 1),
                harvest_date=date(2025, 7, 20),
                storage_requirements="Dry Storage",
                shelf_life="6 months",
                packaging_details="50kg bags"
            )
            db.add_all([prod1, prod2])
            db.commit()

        # 3. Seed Agri Inputs
        if db.query(models.AgriInput).count() == 0:
            input1 = models.AgriInput(
                item="Urea",
                quantity=100.00,
                unit="bags",
                date_received=date(2025, 7, 1),
                input_type="Fertilizer",
                name="Urea 46%",
                stock_level="High",
                usage_rate_per_week="10.00",
                procurement_date=date(2025, 7, 1)
            )
            input2 = models.AgriInput(
                item="Insecticide",
                quantity=25.00,
                unit="liters",
                date_received=date(2025, 7, 5),
                input_type="Chemical",
                name="Lambda-Cyhalothrin",
                stock_level="Medium",
                usage_rate_per_week="3.00",
                procurement_date=date(2025, 7, 5)
            )
            db.add_all([input1, input2])
            db.commit()

        # 4. Seed Harvested Crops
        if db.query(models.HarvestedCrop).count() == 0:
            crop1 = models.HarvestedCrop(
                name="Wheat",
                quantity=1500.00,
                storage_condition="Dry Storage",
                movement_details="Moved to Warehouse A",
                expiry_date=date(2025, 12, 30)
            )
            crop2 = models.HarvestedCrop(
                name="Mangoes",
                quantity=300.00,
                storage_condition="Cold Storage",
                movement_details="Shipped to City Market",
                expiry_date=date(2025, 9, 10)
            )
            db.add_all([crop1, crop2])
            db.commit()

        # 5. Seed Market Data
        if db.query(models.MarketData).count() == 0:
            md1 = models.MarketData(
                market="Mombasa Central",
                product="Maize",
                price_per_unit=0.85,
                date=date(2025, 8, 27)
            )
            md2 = models.MarketData(
                market="Nairobi Wakulima",
                product="Tomato",
                price_per_unit=1.30,
                date=date(2025, 8, 28)
            )
            db.add_all([md1, md2])
            db.commit()
            
    except Exception as e:
        print(f"Error seeding database: {e}")
    finally:
        db.close()


# --- Authentication ---

@app.post("/api/login")
def login(request: schemas.LoginRequest, db: Session = Depends(get_db)):
    user = db.query(models.AdminUser).filter(
        models.AdminUser.username == request.username,
        models.AdminUser.password == request.password
    ).first()
    
    if not user:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Invalid username or password"
        )
    return {"success": True, "username": user.username}


# --- Dashboard ---

@app.get("/api/dashboard", response_model=schemas.DashboardResponse)
def get_dashboard(db: Session = Depends(get_db)):
    products_count = db.query(models.AgriculturalProduct).count()
    agri_inputs_count = db.query(models.AgriInput).count()
    perishables_count = db.query(models.PerishableProduct).count()
    post_harvest_count = db.query(models.PostHarvestMonitor).count()
    
    # Latest 5 market data ordered by ID descending
    market_data = db.query(models.MarketData).order_by(models.MarketData.id.desc()).limit(5).all()
    
    return {
        "productsCount": products_count,
        "agriInputsCount": agri_inputs_count,
        "perishablesCount": perishables_count,
        "postHarvestCount": post_harvest_count,
        "marketData": market_data
    }


# --- 1. Agricultural Products CRUD ---

@app.get("/api/agricultural_products")
def get_agricultural_products(id: Optional[int] = None, db: Session = Depends(get_db)):
    if id is not None:
        item = db.query(models.AgriculturalProduct).filter(models.AgriculturalProduct.id == id).first()
        if not item:
            raise HTTPException(status_code=404, detail="Product not found")
        return item
    return db.query(models.AgriculturalProduct).order_by(models.AgriculturalProduct.id.desc()).all()

@app.post("/api/agricultural_products")
def create_agricultural_product(item: schemas.AgriculturalProductSchema, db: Session = Depends(get_db)):
    db_item = models.AgriculturalProduct(**item.model_dump(exclude={"id"}))
    db.add(db_item)
    db.commit()
    return {"message": "Product created."}

@app.put("/api/agricultural_products")
def update_agricultural_product(item: schemas.AgriculturalProductSchema, db: Session = Depends(get_db)):
    if not item.id:
        raise HTTPException(status_code=400, detail="ID is required for updates")
    db_item = db.query(models.AgriculturalProduct).filter(models.AgriculturalProduct.id == item.id).first()
    if not db_item:
        raise HTTPException(status_code=404, detail="Product not found")
    
    for key, value in item.model_dump(exclude={"id"}).items():
        setattr(db_item, key, value)
    
    db.commit()
    return {"message": "Product updated."}

@app.delete("/api/agricultural_products")
def delete_agricultural_product(req: DeleteRequest, db: Session = Depends(get_db)):
    db_item = db.query(models.AgriculturalProduct).filter(models.AgriculturalProduct.id == req.id).first()
    if not db_item:
        raise HTTPException(status_code=404, detail="Product not found")
    db.delete(db_item)
    db.commit()
    return {"message": "Product deleted."}


# --- 2. Agri Inputs CRUD ---

@app.get("/api/agri_inputs")
def get_agri_inputs(id: Optional[int] = None, db: Session = Depends(get_db)):
    if id is not None:
        item = db.query(models.AgriInput).filter(models.AgriInput.id == id).first()
        if not item:
            raise HTTPException(status_code=404, detail="Input not found")
        return item
    return db.query(models.AgriInput).order_by(models.AgriInput.id.desc()).all()

@app.post("/api/agri_inputs")
def create_agri_input(item: schemas.AgriInputSchema, db: Session = Depends(get_db)):
    db_item = models.AgriInput(**item.model_dump(exclude={"id"}))
    db.add(db_item)
    db.commit()
    return {"message": "Input created."}

@app.put("/api/agri_inputs")
def update_agri_input(item: schemas.AgriInputSchema, db: Session = Depends(get_db)):
    if not item.id:
        raise HTTPException(status_code=400, detail="ID is required for updates")
    db_item = db.query(models.AgriInput).filter(models.AgriInput.id == item.id).first()
    if not db_item:
        raise HTTPException(status_code=404, detail="Input not found")
    
    for key, value in item.model_dump(exclude={"id"}).items():
        setattr(db_item, key, value)
        
    db.commit()
    return {"message": "Input updated."}

@app.delete("/api/agri_inputs")
def delete_agri_input(req: DeleteRequest, db: Session = Depends(get_db)):
    db_item = db.query(models.AgriInput).filter(models.AgriInput.id == req.id).first()
    if not db_item:
        raise HTTPException(status_code=404, detail="Input not found")
    db.delete(db_item)
    db.commit()
    return {"message": "Input deleted."}


# --- 3. Harvested Crops CRUD ---

@app.get("/api/harvested_crops")
def get_harvested_crops(id: Optional[int] = None, db: Session = Depends(get_db)):
    if id is not None:
        item = db.query(models.HarvestedCrop).filter(models.HarvestedCrop.id == id).first()
        if not item:
            raise HTTPException(status_code=404, detail="Crop not found")
        return item
    return db.query(models.HarvestedCrop).order_by(models.HarvestedCrop.id.desc()).all()

@app.post("/api/harvested_crops")
def create_harvested_crop(item: schemas.HarvestedCropSchema, db: Session = Depends(get_db)):
    db_item = models.HarvestedCrop(**item.model_dump(exclude={"id"}))
    db.add(db_item)
    db.commit()
    return {"message": "Crop created."}

@app.put("/api/harvested_crops")
def update_harvested_crop(item: schemas.HarvestedCropSchema, db: Session = Depends(get_db)):
    if not item.id:
        raise HTTPException(status_code=400, detail="ID is required for updates")
    db_item = db.query(models.HarvestedCrop).filter(models.HarvestedCrop.id == item.id).first()
    if not db_item:
        raise HTTPException(status_code=404, detail="Crop not found")
    
    for key, value in item.model_dump(exclude={"id"}).items():
        setattr(db_item, key, value)
        
    db.commit()
    return {"message": "Crop updated."}

@app.delete("/api/harvested_crops")
def delete_harvested_crop(req: DeleteRequest, db: Session = Depends(get_db)):
    db_item = db.query(models.HarvestedCrop).filter(models.HarvestedCrop.id == req.id).first()
    if not db_item:
        raise HTTPException(status_code=404, detail="Crop not found")
    db.delete(db_item)
    db.commit()
    return {"message": "Crop deleted."}


# --- 4. Inventory CRUD ---

@app.get("/api/inventory")
def get_inventory(id: Optional[int] = None, db: Session = Depends(get_db)):
    if id is not None:
        item = db.query(models.Inventory).filter(models.Inventory.id == id).first()
        if not item:
            raise HTTPException(status_code=404, detail="Inventory item not found")
        return item
    return db.query(models.Inventory).order_by(models.Inventory.id.desc()).all()

@app.post("/api/inventory")
def create_inventory_item(item: schemas.InventorySchema, db: Session = Depends(get_db)):
    db_item = models.Inventory(**item.model_dump(exclude={"id"}))
    db.add(db_item)
    db.commit()
    return {"message": "Inventory item created."}

@app.put("/api/inventory")
def update_inventory_item(item: schemas.InventorySchema, db: Session = Depends(get_db)):
    if not item.id:
        raise HTTPException(status_code=400, detail="ID is required for updates")
    db_item = db.query(models.Inventory).filter(models.Inventory.id == item.id).first()
    if not db_item:
        raise HTTPException(status_code=404, detail="Inventory item not found")
    
    for key, value in item.model_dump(exclude={"id"}).items():
        setattr(db_item, key, value)
        
    db.commit()
    return {"message": "Inventory item updated."}

@app.delete("/api/inventory")
def delete_inventory_item(req: DeleteRequest, db: Session = Depends(get_db)):
    db_item = db.query(models.Inventory).filter(models.Inventory.id == req.id).first()
    if not db_item:
        raise HTTPException(status_code=404, detail="Inventory item not found")
    db.delete(db_item)
    db.commit()
    return {"message": "Inventory item deleted."}


# --- 5. Market Data CRUD ---

@app.get("/api/market_data")
def get_market_data(id: Optional[int] = None, db: Session = Depends(get_db)):
    if id is not None:
        item = db.query(models.MarketData).filter(models.MarketData.id == id).first()
        if not item:
            raise HTTPException(status_code=404, detail="Market record not found")
        return item
    return db.query(models.MarketData).order_by(models.MarketData.id.desc()).all()

@app.post("/api/market_data")
def create_market_record(item: schemas.MarketDataSchema, db: Session = Depends(get_db)):
    db_item = models.MarketData(**item.model_dump(exclude={"id"}))
    db.add(db_item)
    db.commit()
    return {"message": "Market record created."}

@app.put("/api/market_data")
def update_market_record(item: schemas.MarketDataSchema, db: Session = Depends(get_db)):
    if not item.id:
        raise HTTPException(status_code=400, detail="ID is required for updates")
    db_item = db.query(models.MarketData).filter(models.MarketData.id == item.id).first()
    if not db_item:
        raise HTTPException(status_code=404, detail="Market record not found")
    
    for key, value in item.model_dump(exclude={"id"}).items():
        setattr(db_item, key, value)
        
    db.commit()
    return {"message": "Market record updated."}

@app.delete("/api/market_data")
def delete_market_record(req: DeleteRequest, db: Session = Depends(get_db)):
    db_item = db.query(models.MarketData).filter(models.MarketData.id == req.id).first()
    if not db_item:
        raise HTTPException(status_code=404, detail="Market record not found")
    db.delete(db_item)
    db.commit()
    return {"message": "Market record deleted."}


# --- 6. Perishable Products CRUD ---

@app.get("/api/perishable_products")
def get_perishable_products(id: Optional[int] = None, db: Session = Depends(get_db)):
    if id is not None:
        item = db.query(models.PerishableProduct).filter(models.PerishableProduct.id == id).first()
        if not item:
            raise HTTPException(status_code=404, detail="Perishable product not found")
        return item
    return db.query(models.PerishableProduct).order_by(models.PerishableProduct.id.desc()).all()

@app.post("/api/perishable_products")
def create_perishable_product(item: schemas.PerishableProductSchema, db: Session = Depends(get_db)):
    db_item = models.PerishableProduct(**item.model_dump(exclude={"id"}))
    db.add(db_item)
    db.commit()
    return {"message": "Perishable product created."}

@app.put("/api/perishable_products")
def update_perishable_product(item: schemas.PerishableProductSchema, db: Session = Depends(get_db)):
    if not item.id:
        raise HTTPException(status_code=400, detail="ID is required for updates")
    db_item = db.query(models.PerishableProduct).filter(models.PerishableProduct.id == item.id).first()
    if not db_item:
        raise HTTPException(status_code=404, detail="Perishable product not found")
    
    for key, value in item.model_dump(exclude={"id"}).items():
        setattr(db_item, key, value)
        
    db.commit()
    return {"message": "Perishable product updated."}

@app.delete("/api/perishable_products")
def delete_perishable_product(req: DeleteRequest, db: Session = Depends(get_db)):
    db_item = db.query(models.PerishableProduct).filter(models.PerishableProduct.id == req.id).first()
    if not db_item:
        raise HTTPException(status_code=404, detail="Perishable product not found")
    db.delete(db_item)
    db.commit()
    return {"message": "Perishable product deleted."}


# --- 7. Post Harvest Monitor CRUD ---

@app.get("/api/post_harvest_monitor")
def get_post_harvest_monitors(id: Optional[int] = None, db: Session = Depends(get_db)):
    if id is not None:
        item = db.query(models.PostHarvestMonitor).filter(models.PostHarvestMonitor.id == id).first()
        if not item:
            raise HTTPException(status_code=404, detail="Post-harvest inspection not found")
        return item
    return db.query(models.PostHarvestMonitor).order_by(models.PostHarvestMonitor.id.desc()).all()

@app.post("/api/post_harvest_monitor")
def create_post_harvest_monitor(item: schemas.PostHarvestMonitorSchema, db: Session = Depends(get_db)):
    db_item = models.PostHarvestMonitor(**item.model_dump(exclude={"id"}))
    db.add(db_item)
    db.commit()
    return {"message": "Inspection recorded."}

@app.put("/api/post_harvest_monitor")
def update_post_harvest_monitor(item: schemas.PostHarvestMonitorSchema, db: Session = Depends(get_db)):
    if not item.id:
        raise HTTPException(status_code=400, detail="ID is required for updates")
    db_item = db.query(models.PostHarvestMonitor).filter(models.PostHarvestMonitor.id == item.id).first()
    if not db_item:
        raise HTTPException(status_code=404, detail="Post-harvest inspection not found")
    
    for key, value in item.model_dump(exclude={"id"}).items():
        setattr(db_item, key, value)
        
    db.commit()
    return {"message": "Inspection updated."}

@app.delete("/api/post_harvest_monitor")
def delete_post_harvest_monitor(req: DeleteRequest, db: Session = Depends(get_db)):
    db_item = db.query(models.PostHarvestMonitor).filter(models.PostHarvestMonitor.id == req.id).first()
    if not db_item:
        raise HTTPException(status_code=404, detail="Post-harvest inspection not found")
    db.delete(db_item)
    db.commit()
    return {"message": "Inspection deleted."}


# --- 8. Storage Conditions CRUD ---

@app.get("/api/storage_conditions")
def get_storage_conditions(id: Optional[int] = None, db: Session = Depends(get_db)):
    if id is not None:
        item = db.query(models.StorageCondition).filter(models.StorageCondition.id == id).first()
        if not item:
            raise HTTPException(status_code=404, detail="Storage facility conditions not found")
        return item
    return db.query(models.StorageCondition).order_by(models.StorageCondition.id.desc()).all()

@app.post("/api/storage_conditions")
def create_storage_condition(item: schemas.StorageConditionSchema, db: Session = Depends(get_db)):
    db_item = models.StorageCondition(**item.model_dump(exclude={"id"}))
    db.add(db_item)
    db.commit()
    return {"message": "Storage facility conditions recorded."}

@app.put("/api/storage_conditions")
def update_storage_condition(item: schemas.StorageConditionSchema, db: Session = Depends(get_db)):
    if not item.id:
        raise HTTPException(status_code=400, detail="ID is required for updates")
    db_item = db.query(models.StorageCondition).filter(models.StorageCondition.id == item.id).first()
    if not db_item:
        raise HTTPException(status_code=404, detail="Storage facility conditions not found")
    
    for key, value in item.model_dump(exclude={"id"}).items():
        setattr(db_item, key, value)
        
    db.commit()
    return {"message": "Storage facility conditions updated."}

@app.delete("/api/storage_conditions")
def delete_storage_condition(req: DeleteRequest, db: Session = Depends(get_db)):
    db_item = db.query(models.StorageCondition).filter(models.StorageCondition.id == req.id).first()
    if not db_item:
        raise HTTPException(status_code=404, detail="Storage facility conditions not found")
    db.delete(db_item)
    db.commit()
    return {"message": "Storage facility conditions deleted."}


# --- 9. Tracking of Products CRUD ---

@app.get("/api/tracking_of_products")
def get_tracking_of_products(id: Optional[int] = None, db: Session = Depends(get_db)):
    if id is not None:
        item = db.query(models.TrackingOfProduct).filter(models.TrackingOfProduct.id == id).first()
        if not item:
            raise HTTPException(status_code=404, detail="Tracking record not found")
        return item
    return db.query(models.TrackingOfProduct).order_by(models.TrackingOfProduct.id.desc()).all()

@app.post("/api/tracking_of_products")
def create_tracking_record(item: schemas.TrackingOfProductSchema, db: Session = Depends(get_db)):
    db_item = models.TrackingOfProduct(**item.model_dump(exclude={"id"}))
    db.add(db_item)
    db.commit()
    return {"message": "Tracking record created."}

@app.put("/api/tracking_of_products")
def update_tracking_record(item: schemas.TrackingOfProductSchema, db: Session = Depends(get_db)):
    if not item.id:
        raise HTTPException(status_code=400, detail="ID is required for updates")
    db_item = db.query(models.TrackingOfProduct).filter(models.TrackingOfProduct.id == item.id).first()
    if not db_item:
        raise HTTPException(status_code=404, detail="Tracking record not found")
    
    for key, value in item.model_dump(exclude={"id"}).items():
        setattr(db_item, key, value)
        
    db.commit()
    return {"message": "Tracking record updated."}

@app.delete("/api/tracking_of_products")
def delete_tracking_record(req: DeleteRequest, db: Session = Depends(get_db)):
    db_item = db.query(models.TrackingOfProduct).filter(models.TrackingOfProduct.id == req.id).first()
    if not db_item:
        raise HTTPException(status_code=404, detail="Tracking record not found")
    db.delete(db_item)
    db.commit()
    return {"message": "Tracking record deleted."}

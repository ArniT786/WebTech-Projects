from sqlalchemy import Column, Integer, String, Float, Text, Date
from database import Base

class AdminUser(Base):
    __tablename__ = "admin_users"
    id = Column(Integer, primary_key=True, index=True)
    username = Column(String(255), unique=True, nullable=False, index=True)
    password = Column(String(255), nullable=False)

class AgriculturalProduct(Base):
    __tablename__ = "agricultural_products"
    id = Column(Integer, primary_key=True, index=True)
    product_name = Column(String(255), nullable=False)
    category = Column(String(255), nullable=False)
    growing_date = Column(Date, nullable=True)
    harvest_date = Column(Date, nullable=True)
    storage_requirements = Column(String(255), nullable=True)
    shelf_life = Column(String(255), nullable=True)
    packaging_details = Column(String(255), nullable=True)

class AgriInput(Base):
    __tablename__ = "agri_inputs"
    id = Column(Integer, primary_key=True, index=True)
    item = Column(String(255), nullable=False)
    quantity = Column(Float, nullable=False)
    unit = Column(String(50), nullable=False)
    date_received = Column(Date, nullable=True)
    input_type = Column(String(255), nullable=True)
    name = Column(String(255), nullable=False)
    stock_level = Column(String(100), nullable=True)
    usage_rate_per_week = Column(String(100), nullable=True)
    procurement_date = Column(Date, nullable=True)

class HarvestedCrop(Base):
    __tablename__ = "harvested_crops"
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String(255), nullable=False)
    quantity = Column(Float, nullable=False)
    storage_condition = Column(String(255), nullable=True)
    movement_details = Column(Text, nullable=True)
    expiry_date = Column(Date, nullable=True)

class Inventory(Base):
    __tablename__ = "inventory"
    id = Column(Integer, primary_key=True, index=True)
    item_name = Column(String(255), nullable=False)
    amount = Column(Float, nullable=False)
    unit = Column(String(50), nullable=False)
    date_entered = Column(Date, nullable=True)
    expiry_date = Column(Date, nullable=True)
    destination = Column(String(255), nullable=True)
    warehouse = Column(String(255), nullable=True)
    notes = Column(Text, nullable=True)

class MarketData(Base):
    __tablename__ = "market_data"
    id = Column(Integer, primary_key=True, index=True)
    market = Column(String(255), nullable=False)
    product = Column(String(255), nullable=False)
    price_per_unit = Column(Float, nullable=False)
    date = Column(Date, nullable=True)

class PerishableProduct(Base):
    __tablename__ = "perishable_products"
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String(255), nullable=False)
    batch_number = Column(String(100), nullable=True)
    storage_temp = Column(String(100), nullable=True)
    shelf_life_days = Column(Integer, nullable=True)
    status = Column(String(100), nullable=True)
    added_date = Column(Date, nullable=True)

class PostHarvestMonitor(Base):
    __tablename__ = "post_harvest_monitor"
    id = Column(Integer, primary_key=True, index=True)
    crop_name = Column(String(255), nullable=False)
    moisture_level = Column(String(100), nullable=True)
    temperature = Column(String(100), nullable=True)
    visual_inspection = Column(String(255), nullable=True)
    inspection_date = Column(Date, nullable=True)
    inspector = Column(String(255), nullable=True)

class StorageCondition(Base):
    __tablename__ = "storage_conditions"
    id = Column(Integer, primary_key=True, index=True)
    facility_name = Column(String(255), nullable=False)
    current_temp = Column(String(100), nullable=True)
    humidity = Column(String(100), nullable=True)
    ventilation_status = Column(String(100), nullable=True)
    last_checked = Column(Date, nullable=True)

class TrackingOfProduct(Base):
    __tablename__ = "tracking_of_products"
    id = Column(Integer, primary_key=True, index=True)
    product_name = Column(String(255), nullable=False)
    current_location = Column(String(255), nullable=True)
    destination = Column(String(255), nullable=True)
    transit_status = Column(String(100), nullable=True)
    dispatch_date = Column(Date, nullable=True)

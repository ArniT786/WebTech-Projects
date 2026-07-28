from pydantic import BaseModel, field_validator
from datetime import date, datetime
from typing import Optional, List, Dict, Any

def normalize_date(v):
    if v == "" or v is None:
        return None
    if isinstance(v, datetime):
        return v.date()
    if isinstance(v, date):
        return v
    if isinstance(v, str):
        # Strip time or timezone info if present (e.g. T19:04:13.251Z)
        if "T" in v:
            v = v.split("T")[0]
        elif " " in v:
            v = v.split(" ")[0]
        try:
            return datetime.strptime(v, "%Y-%m-%d").date()
        except ValueError:
            return None
    return v

class LoginRequest(BaseModel):
    username: str
    password: str

class AgriculturalProductSchema(BaseModel):
    id: Optional[int] = None
    product_name: str
    category: str
    growing_date: Optional[date] = None
    harvest_date: Optional[date] = None
    storage_requirements: Optional[str] = None
    shelf_life: Optional[str] = None
    packaging_details: Optional[str] = None

    @field_validator('growing_date', 'harvest_date', mode='before')
    @classmethod
    def check_date(cls, v):
        return normalize_date(v)

    class Config:
        from_attributes = True

class AgriInputSchema(BaseModel):
    id: Optional[int] = None
    item: str
    quantity: float
    unit: str
    date_received: Optional[date] = None
    input_type: Optional[str] = None
    name: str
    stock_level: Optional[str] = None
    usage_rate_per_week: Optional[str] = None
    procurement_date: Optional[date] = None

    @field_validator('date_received', 'procurement_date', mode='before')
    @classmethod
    def check_date(cls, v):
        return normalize_date(v)

    class Config:
        from_attributes = True

class HarvestedCropSchema(BaseModel):
    id: Optional[int] = None
    name: str
    quantity: float
    storage_condition: Optional[str] = None
    movement_details: Optional[str] = None
    expiry_date: Optional[date] = None

    @field_validator('expiry_date', mode='before')
    @classmethod
    def check_date(cls, v):
        return normalize_date(v)

    class Config:
        from_attributes = True

class InventorySchema(BaseModel):
    id: Optional[int] = None
    item_name: str
    amount: float
    unit: str
    date_entered: Optional[date] = None
    expiry_date: Optional[date] = None
    destination: Optional[str] = None
    warehouse: Optional[str] = None
    notes: Optional[str] = None

    @field_validator('date_entered', 'expiry_date', mode='before')
    @classmethod
    def check_date(cls, v):
        return normalize_date(v)

    class Config:
        from_attributes = True

class MarketDataSchema(BaseModel):
    id: Optional[int] = None
    market: str
    product: str
    price_per_unit: float
    date: Optional[date] = None

    @field_validator('date', mode='before')
    @classmethod
    def check_date(cls, v):
        return normalize_date(v)

    class Config:
        from_attributes = True

class PerishableProductSchema(BaseModel):
    id: Optional[int] = None
    name: str
    batch_number: Optional[str] = None
    storage_temp: Optional[str] = None
    shelf_life_days: Optional[int] = None
    status: Optional[str] = None
    added_date: Optional[date] = None

    @field_validator('added_date', mode='before')
    @classmethod
    def check_date(cls, v):
        return normalize_date(v)

    @field_validator('shelf_life_days', mode='before')
    @classmethod
    def check_int(cls, v):
        if v == "":
            return None
        return v

    class Config:
        from_attributes = True

class PostHarvestMonitorSchema(BaseModel):
    id: Optional[int] = None
    crop_name: str
    moisture_level: Optional[str] = None
    temperature: Optional[str] = None
    visual_inspection: Optional[str] = None
    inspection_date: Optional[date] = None
    inspector: Optional[str] = None

    @field_validator('inspection_date', mode='before')
    @classmethod
    def check_date(cls, v):
        return normalize_date(v)

    class Config:
        from_attributes = True

class StorageConditionSchema(BaseModel):
    id: Optional[int] = None
    facility_name: str
    current_temp: Optional[str] = None
    humidity: Optional[str] = None
    ventilation_status: Optional[str] = None
    last_checked: Optional[date] = None

    @field_validator('last_checked', mode='before')
    @classmethod
    def check_date(cls, v):
        return normalize_date(v)

    class Config:
        from_attributes = True

class TrackingOfProductSchema(BaseModel):
    id: Optional[int] = None
    product_name: str
    current_location: Optional[str] = None
    destination: Optional[str] = None
    transit_status: Optional[str] = None
    dispatch_date: Optional[date] = None

    @field_validator('dispatch_date', mode='before')
    @classmethod
    def check_date(cls, v):
        return normalize_date(v)

    class Config:
        from_attributes = True

class DashboardResponse(BaseModel):
    productsCount: int
    agriInputsCount: int
    perishablesCount: int
    postHarvestCount: int
    marketData: List[MarketDataSchema]

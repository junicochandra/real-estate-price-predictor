from dataclasses import dataclass
from typing import Optional
from datetime import datetime


@dataclass
class House:
    id: Optional[int] = None
    address: Optional[str] = None
    city: str = ""
    state: Optional[str] = None
    zip_code: Optional[str] = None
    bedrooms: int = 0
    bathrooms: float = 0
    year_built: Optional[int] = None
    lot_size_m2: Optional[float] = None
    has_garage: bool = False
    has_pool: bool = False
    predicted_price: Optional[float] = None
    actual_price: Optional[float] = None
    created_at: Optional[datetime] = None
    updated_at: Optional[datetime] = None

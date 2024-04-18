from datetime import datetime
from typing import Optional
from pydantic import BaseModel


class RatingBase(BaseModel):
    rating: int
    comment: Optional[str] = None


class RatingCreate(RatingBase):
    pass


class RatingUpdate(BaseModel):
    rating: Optional[str] = None
    comment: Optional[str] = None


class Order(RatingBase):
    id: int
    customer_id: int
    order_id: int
    timestamp: Optional[datetime] = None

    class ConfigDict:
        from_attributes = True
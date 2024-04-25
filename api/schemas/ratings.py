from datetime import datetime
from typing import Optional
from pydantic import BaseModel


class RatingBase(BaseModel):
    customer_id: int
    order_id: int
    rating: int
    comment: Optional[str] = None


class RatingCreate(RatingBase):
    pass


class RatingUpdate(BaseModel):
    rating: Optional[str] = None
    comment: Optional[str] = None


class Rating(RatingBase):
    id: int
    timestamp: Optional[datetime] = None

    class ConfigDict:
        from_attributes = True
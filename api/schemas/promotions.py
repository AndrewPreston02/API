from datetime import date
from typing import Optional
from pydantic import BaseModel


class PromotionBase(BaseModel):
    discount: float
    expiration_date: Optional[date] = None


class PromotionCreate(PromotionBase):
    pass


class PromotionUpdate(BaseModel):
    discount: Optional[float] = None
    expiration_date: Optional[date] = None


class Promotion(PromotionBase):
    id: int

    class Config:
        orm_mode = True

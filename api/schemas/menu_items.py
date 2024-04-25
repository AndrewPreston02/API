from typing import List, Optional
from pydantic import BaseModel


class MenuItemBase(BaseModel):
    name: str
    price: float
    calories: Optional[int] = None
    ingredients: Optional[str] = None
    category: Optional[str] = None
    dishes: Optional[str] = None


class MenuItemCreate(MenuItemBase):
    pass


class MenuItemUpdate(BaseModel):
    name: Optional[str] = None
    price: Optional[float] = None
    calories: Optional[int] = None
    ingredients: Optional[str] = None
    category: Optional[str] = None
    dishes: Optional[str] = None


class MenuItem(MenuItemBase):
    id: int

    class Config:
        orm_mode = True

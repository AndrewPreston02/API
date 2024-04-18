from datetime import datetime
from typing import Optional
from pydantic import BaseModel


class ResourceBase(BaseModel):
    unit: str
    amount: int


class ResourceCreate(ResourceBase):
    pass


class ResourceUpdate(BaseModel):
    unit: Optional[str] = None
    amount: Optional[int] = None


class Resource(ResourceBase):
    id: int

    class ConfigDict:
        from_attributes = True

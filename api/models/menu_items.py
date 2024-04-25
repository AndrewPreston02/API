from sqlalchemy import Column, ForeignKey, Integer, String, DECIMAL
from sqlalchemy.orm import relationship

from ..dependencies.database import Base


class MenuItem(Base):
    __tablename__ = "menu_items"

    id = Column(Integer, primary_key=True, index=True, autoincrement=True)
    name = Column(String(100), index=True, nullable=False)
    calories = Column(Integer, nullable=False)
    category = Column(String(50), nullable=False)
    ingredients = Column(String(500), nullable=False)
    dishes = Column(String(500), nullable=False)
    price = Column(DECIMAL(10, 2), nullable=False)

    resources = relationship("Resource", back_populates="menu_item")

from sqlalchemy import Column, Integer, String, DECIMAL, DATE
from ..dependencies.database import Base
from datetime import datetime


class Promotion(Base):
    __tablename__ = "promotions"

    id = Column(Integer, primary_key=True, index=True, autoincrement=True)
    discount = Column(DECIMAL, unique=True, index=True)
    expiration_date = Column(DATE, nullable=False)

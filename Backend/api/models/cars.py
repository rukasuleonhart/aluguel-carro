from datetime import datetime
from typing import List
from sqlalchemy import String, Float, Integer, ARRAY, DateTime, func
from sqlalchemy.orm import Mapped, mapped_column, relationship
from models.base import Base

class Car(Base):
    __tablename__ = "cars"

    id: Mapped[int] = mapped_column(primary_key=True, index=True)
    brand: Mapped[str] = mapped_column(String)
    model: Mapped[str] = mapped_column(String)
    price: Mapped[float] = mapped_column(Float)
    images: Mapped[List[str]] = mapped_column(ARRAY(String))  # Compatível com PostgreSQL
    speed: Mapped[str] = mapped_column(String)
    acceleration: Mapped[str] = mapped_column(String)
    fuel: Mapped[str] = mapped_column(String)
    transmission: Mapped[str] = mapped_column(String)
    horsepower: Mapped[str] = mapped_column(String)
    seats: Mapped[int] = mapped_column(Integer)

    created_at: Mapped[datetime] = mapped_column(
        DateTime, server_default=func.now()
    )
    updated_at: Mapped[datetime] = mapped_column(
        DateTime, server_default=func.now(), onupdate=func.now()
    )

    rentals = relationship("Rental", back_populates="car")

from sqlalchemy import Column, Integer, Float, String

from base.base import Base


class LocationModel(Base):
    __tablename__ = 'location'
    id = Column(Integer, primary_key=True)
    latitude = Column(Float)
    longitude = Column(Float)
    city = Column(String)
    country = Column(String)


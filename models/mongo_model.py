from sqlalchemy import Column, Integer, String, DateTime

from base.base import Base


class HostageModel(Base):
    __tablename__ = 'hostages'
    id = Column(Integer, primary_key=True)
    email = Column(String, nullable=False)
    sentence = Column(String, nullable=False)
    detected_at = Column(DateTime)

class ExplosiveModel(Base):
    __tablename__ = 'explosives'
    id = Column(Integer, primary_key=True)
    email = Column(String, nullable=False)
    sentence = Column(String, nullable=False)
    detected_at = Column(DateTime)
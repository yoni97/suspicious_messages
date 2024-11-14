from sqlalchemy import Column, Integer, String, DateTime, JSON
from sqlalchemy.orm import relationship

from base.base import Base


class EmailModel(Base):
    __tablename__ = 'emails'

    id = Column(Integer, primary_key=True)
    email = Column(String)
    username = Column(String)
    ip_address = Column(String)
    created_at = Column(String)
    location = Column(JSON)
    device_info = Column(JSON)
    sentences = Column(JSON)

    hostages = relationship('HostageModel', back_populates='email')
    explos = relationship('ExplosModel', back_populates='email')
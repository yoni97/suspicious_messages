from sqlalchemy import Column, Integer, ForeignKey
from sqlalchemy.orm import relationship

from base.base import Base

class HostageModel(Base):
    __tablename__ = 'hostages'

    id = Column(Integer, primary_key=True) # PK int
    email_id = Column(Integer, ForeignKey("emails.id"))

    email = relationship("EmailsModel", back_populates="hostages")
from sqlalchemy import Column, Integer, ForeignKey
from sqlalchemy.orm import relationship

from base.base import Base


class ExplosModel(Base):
    __tablename__ = 'explos'

    id = Column(Integer, primary_key=True)
    email_id = Column(Integer, ForeignKey("emails.id"))

    email = relationship("EmailsModel", back_populates="explos")
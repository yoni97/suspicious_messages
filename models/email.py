from sqlalchemy import Column, Integer, String, DateTime

from base.base import Base


class EmailModel(Base):
    __tablename__ = 'email'
    id = Column(Integer, primary_key=True)
    email = Column(String)
    username = Column(String)
    ip_address = Column(String)
    created_at = Column(DateTime)
    # location =
    # device_info =
    # sentences =
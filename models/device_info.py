from sqlalchemy import Column, Integer, String

from base.base import Base


class DeviceInfoModel(Base):
    __tablename__ = 'device_info'
    id = Column(Integer, primary_key=True)
    browser = Column(String)
    os = Column(String)
    device_id = Column(String)
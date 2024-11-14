from sqlalchemy import Column, Integer, String, DateTime

from base.base import Base
from models.device_info import DeviceInfoModel
from models.location import LocationModel
from models.sentences import SentencesModel


class EmailModel(Base):
    __tablename__ = 'email'
    id = Column(Integer, primary_key=True)
    email = Column(String)
    username = Column(String)
    ip_address = Column(String)
    created_at = Column(DateTime)
    location = LocationModel
    device_info = DeviceInfoModel
    sentences = SentencesModel
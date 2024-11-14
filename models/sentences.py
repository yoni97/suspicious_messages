from sqlalchemy import Column, Integer, ForeignKey

from base.base import Base


class SentencesModel(Base):
    __tablename__ = 'sentences'
    id = Column(Integer, primary_key=True)
    sentences = []
from sqlalchemy import Column, Integer, String

from data_shared.base import Base


class Country(Base):
    __tablename__ = "countries"
    id = Column(Integer, primary_key=True)
    name = Column(String, nullable=False)
    iso_code = Column(String, nullable=False)

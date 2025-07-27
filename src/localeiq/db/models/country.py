from sqlalchemy import Column, String
from localeiq.db.base import Base


class Country(Base):
    __tablename__ = "countries"

    code = Column(String(2), primary_key=True, index=True)  # ISO 3166-1 alpha-2
    name = Column(String, nullable=False)

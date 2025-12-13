from sqlalchemy import Integer, Column, String, Text

from data_store.schema.base import Base
from data_store.schema.bronze_provenance_mixin import BronzeProvenanceMixin


class LanguageBronzeSchema(BronzeProvenanceMixin, Base):
    __tablename__ = "languages"
    __table_args__ = {
        "schema": "bronze",
        "comment": "Raw language data from various sources",
    }

    id = Column(Integer, primary_key=True)
    iso_639_1 = Column(
        String(64),
        nullable=False,
        comment="ISO 639-1 two-letter code for major languages: en, zh, fr, etc.",
    )
    iso_639_2 = Column(
        String(64),
        nullable=False,
        comment="ISO 639-2 three-letter code for wider range of languages including language groups: eng, chi, fre, etc.",
    )
    name = Column(String(256), nullable=False, comment="English name of the language")
    name_local = Column(
        String(256), nullable=True, comment="Native name of the language"
    )
    script = Column(String(32), nullable=True, comment="Script used in the language")
    direction = Column(
        String(8), nullable=True, comment="Text direction of the language"
    )
    notes = Column(Text, nullable=True, comment="Optional notes about the record")

    def __repr__(self):
        return f"<bronze.language(id={self.id}, iso_639_1={self.iso_639_1}, name={self.name})>"

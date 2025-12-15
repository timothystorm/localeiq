from sqlalchemy import Column, Integer, String, Index
from sqlalchemy.testing.schema import mapped_column

from data_store.schema.base import Base
from data_store.schema.bronze_provenance_mixin import BronzeProvenanceMixin


class LocaleBronzeLocale(BronzeProvenanceMixin, Base):
    __tablename__ = "locale"
    __table_args__ = (
        Index("idx_locale_tag", "tag"),
        Index("idx_locale_language", "language"),
        Index("idx_locale_region", "region"),
        {"schema": "bronze", "comment": "Canonical locale identifiers (BCP 47 / CLDR)"},
    )

    id = Column(Integer, primary_key=True)
    tag = mapped_column(
        String(32),
        nullable=False,
        unique=True,
        comment="BCP-47 language tag with optional script: es-MX, en-US, en-Latn-US, zh_Hans_CN",
    )
    language = mapped_column(
        String(16), nullable=False, comment="Language code: es, en, zh"
    )
    region = mapped_column(String(16), nullable=True, comment="Region code: US, MX, CN")
    script = mapped_column(
        String(16), nullable=True, comment="Language script: Latn, Hans, Cyrl"
    )

    def __repr__(self):
        return (
            f"<bronze.locale(id={self.id}, tag={self.tag}, source={self.source_name})>"
        )

from sqlalchemy import Column, Integer, String, Index
from sqlalchemy.testing.schema import mapped_column

from data_store.schema.base import Base
from data_store.schema.bronze.bronze_provenance_mixin import BronzeProvenanceMixin


class LocaleBronzeSchema(BronzeProvenanceMixin, Base):
    """
    Raw locale data from various sources. There may be duplications and contradictions that need to be resolved in later medallion layers.
    """

    __tablename__ = "locales"
    __table_args__ = (
        Index("idx_locale", "locale"),
        Index("idx_locale_language", "language"),
        Index("idx_locale_script", "script"),
        Index("idx_locale_region", "region"),
        {"schema": "bronze", "comment": "Raw locale data from various sources."},
    )

    id = Column(Integer, primary_key=True)
    locale = mapped_column(
        String(32),
        comment="locale tag: en, es-MX, en-US, en-Latn-US, zh_Hans_CN, zh",
    )
    language = mapped_column(
        String(16),
        nullable=True,
        comment="Primary language subtag: 'en', 'es', 'zh'",
    )
    script = mapped_column(
        String(16),
        nullable=True,
        comment="Optional script subtag: 'Latn', 'Hans', 'Cyrl'",
    )
    region = mapped_column(
        String(16),
        nullable=True,
        comment="Optional region subtag: 'US', 'MX', 'CN'",
    )

    def __repr__(self):
        parent = f"\n↑↑{super().__repr__()}" if super().__repr__() else ""
        return f"<bronze.locale(id={self.id}, locale={self.locale}, language={self.language}, script={self.script}, region={self.region})>{parent}"

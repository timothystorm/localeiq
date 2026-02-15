from sqlalchemy import Integer, Column, String
from sqlalchemy.orm import mapped_column

from data_store.schema.base import Base
from data_store.schema.bronze.bronze_provenance_mixin import BronzeProvenanceMixin


class LanguageBronzeSchema(BronzeProvenanceMixin, Base):
    """
    Raw language data from various sources. There may be duplications and contradictions that need to be resolved in later medallion layers.
    """

    __tablename__ = "languages"
    __table_args__ = {
        "schema": "bronze",
        "comment": "Raw language data from various sources.",
    }

    id = mapped_column(Integer, primary_key=True)
    locale = mapped_column(
        String(32),
        nullable=True,
        comment="Locale code associated with the language and determines label regionally",
    )
    language_code = Column(
        String(64),
        nullable=False,
        comment="Unique code representing the language from the source system",
    )
    label = mapped_column(
        String(128),
        nullable=False,
        comment="Human-readable language label as asserted by the source",
    )

    """
    Data source classification. Examples include:
    
    - cldr:menu:core
    - cldr:menu:extension
    - cldr:alt:menu
    - cldr:alt:variant
    - ethnologue:primary
    - ethnologue:alternate
    """
    source_category = mapped_column(
        String(64),
        nullable=True,
        comment="Source-specific classification (opaque). Examples: menu.core, alt.variant",
    )
    assertion_type = mapped_column(
        String(32),
        nullable=False,
        default="label",
        comment="Nature of the assertion (e.g., label, alias, variant, menu_hint)",
    )

    def __repr__(self):
        parent = f"\n↑↑{super().__repr__()}" if super().__repr__() else ""
        return f"<bronze.language(id={self.id}, language_code={self.language_code}, label={self.label}, locale={self.locale})>{parent}"

import uuid

from sqlalchemy import Column, String, UUID, DateTime, func, Text

from data_shared.base import Base


class CountryBronze(Base):
    __tablename__ = "countries"
    __table_args__ = {
        "schema": "bronze",
        "comment": "Raw country data from various sources",
    }

    id = Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)
    # source_record_id = Column(String(128), nullable=True)  # e.g., a CLDR ID or wiki slug
    name = Column(String(256), nullable=False, comment="Raw country name from source")
    iso_alpha_2 = Column(String(2), nullable=True, comment="e.g., 'US', 'CA'")
    iso_alpha_3 = Column(String(3), nullable=True, comment="e.g., 'USA', 'CAN'")
    iso_num = Column(String(3), nullable=True, comment="e.g., '840', '124'")
    source_name = Column(
        String(64), nullable=False, comment="'CLDR', 'Wikipedia', etc."
    )
    notes = Column(Text, nullable=True, comment="Optional notes about the record")

    # Language/culture (for later mapping)
    # language = Column(String(16), nullable=True)  # e.g., "en", "es", etc.
    # script = Column(String(32), nullable=True)  # e.g., "Latn", "Cyrl"
    # Store raw blob if needed (good for patching or recovery)
    # raw_data = Column(JSON, nullable=True)

    # Metadata
    created_at = Column(
        DateTime(timezone=True), server_default=func.now(), nullable=False
    )
    updated_at = Column(
        DateTime(timezone=True), server_default=func.now(), onupdate=func.now()
    )

    def __repr__(self):
        return f"<bronze.country(id={self.id}, name={self.name}, source={self.source_name})>"

import uuid

from sqlalchemy import String, UUID, Text
from sqlalchemy.orm import mapped_column

from data_store.schema.base import Base
from data_store.schema.bronze.bronze_provenance_mixin import BronzeProvenanceMixin


class CountryBronzeSchema(BronzeProvenanceMixin, Base):
    __tablename__ = "countries"
    __table_args__ = {
        "schema": "bronze",
        "comment": "Raw country data from various sources",
    }

    id = mapped_column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)
    # source_record_id = Column(String(128), nullable=True)  # e.g., a CLDR ID or wiki slug
    name = mapped_column(
        String(256), nullable=False, comment="Raw country name from source"
    )
    iso_alpha_2 = mapped_column(String(2), nullable=True, comment="e.g., 'US', 'CA'")
    iso_alpha_3 = mapped_column(String(3), nullable=True, comment="e.g., 'USA', 'CAN'")
    iso_num = mapped_column(String(3), nullable=True, comment="e.g., '840', '124'")
    notes = mapped_column(
        Text, nullable=True, comment="Optional notes about the record"
    )
    # raw_data = Column(JSON, nullable=True)

    def __repr__(self):
        return f"<bronze.country(id={self.id}, name={self.name}, source={self.source_name})>"

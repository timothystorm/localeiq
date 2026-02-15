from sqlalchemy import String, Text, DateTime, func
from sqlalchemy.orm import mapped_column


class BronzeProvenanceMixin:
    """
    Adds provenance and audit columns to bronze layer tables
    """

    # Provenance - where did this data come from?
    source_name = mapped_column(
        String(64), nullable=False, comment="Source of data: 'cldr', 'Wikipedia', etc."
    )
    source_version = mapped_column(
        String(32), nullable=True, comment="Version of the source data, if applicable"
    )
    source_url = mapped_column(
        String(256), nullable=True, comment="URL or location of the source data"
    )
    source_path = mapped_column(
        String(128),
        nullable=True,
        comment="Path within the source data where this locale is defined, if applicable",
    )
    notes = mapped_column(
        Text, nullable=True, comment="Optional notes about the record"
    )

    # Audit metadata
    created_at = mapped_column(
        DateTime(timezone=True), server_default=func.now(), nullable=False
    )
    updated_at = mapped_column(
        DateTime(timezone=True), server_default=func.now(), onupdate=func.now()
    )

    def __repr__(self):
        return f"<bronze.provenance(source_name={self.source_name}, source_version={self.source_version}, source_url={self.source_url})>"

from sqlalchemy import String, Text, DateTime, func
from sqlalchemy.orm import mapped_column


class BronzeProvenanceMixin:
    """
    Adds provenance and audit columns to bronze layer tables
    """

    # Provenance
    source_name = mapped_column(
        String(64), nullable=False, comment="'CLDR', 'Wikipedia', etc."
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

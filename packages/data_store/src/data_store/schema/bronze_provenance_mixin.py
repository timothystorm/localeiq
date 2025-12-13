from sqlalchemy import Column, String, Text, DateTime, func


class BronzeProvenanceMixin:
    """
    Adds provenance and audit columns to bronze layer tables
    """

    # Provenance
    source_name = Column(
        String(64), nullable=False, comment="'CLDR', 'Wikipedia', etc."
    )
    notes = Column(Text, nullable=True, comment="Optional notes about the record")

    # Audit metadata
    created_at = Column(
        DateTime(timezone=True), server_default=func.now(), nullable=False
    )
    updated_at = Column(
        DateTime(timezone=True), server_default=func.now(), onupdate=func.now()
    )

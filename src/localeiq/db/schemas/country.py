from sqlalchemy import Column, Integer, String, Boolean, TIMESTAMP, func, ForeignKey, Text, CheckConstraint
from sqlalchemy.orm import relationship

from localeiq.db.base import Base


class CountrySchema(Base):
    __tablename__ = "country"

    id = Column(Integer, primary_key=True)
    iso_alpha2 = Column(
        String(2), unique=True, nullable=False, index=True
    )  # ISO 3166-1 alpha-2 - ex. US, CA, GB
    iso_alpha3 = Column(
        String(3), unique=True, nullable=False, index=True
    )  # ISO 3166-1 alpha-3 - ex. USA, CAN, GBR
    iso_numeric = Column(
        String(3), unique=True, nullable=False
    )  # ISO 3166-1 numeric - ex. 840, 124, 826
    sovereign = Column(Boolean, default=True)  # Is this a sovereign country?
    is_disputed = Column(Boolean, default=False)  # ex. Macau, Taiwan

    # relationships
    # meta = relationship("CountryMetaSchema", back_populates="country", uselist=False)
    localized_names = relationship(
        "CountryLocalizedNameSchema", back_populates="country"
    )

    # audit fields
    created_at = Column(TIMESTAMP, server_default=func.now())
    updated_at = Column(TIMESTAMP, server_default=func.now(), onupdate=func.now())


# class CountryMetaSchema(Base):
#     __tablename__ = "country_meta"
#
#     id = Column(Integer, primary_key=True)
#     country_id = Column(Integer, ForeignKey("country.id", ondelete="CASCADE"))
#     currency_code = Column(
#         String(3)
#     )  # ISO 4217 currency code, e.g. 'USD', 'EUR', 'GBP'
#     currency_name = Column(Text)  # e.g. 'United States Dollar', 'Euro', 'British Pound'
#     currency_symbol = Column(Text)  # e.g. '$', '€', '£'`
#     calling_codes = Column(ARRAY(Text))  # e.g. ['+1', '+44', '+33']
#     timezones = Column(
#         ARRAY(Text)
#     )  # IANA time zone identifiers, e.g. ['America/New_York', 'Europe/London']
#     languages = Column(ARRAY(Text))  # ISO 639-1 codes, e.g. ['en', 'fr', 'es']
#     driving_side = Column(Text)  # 'left' or 'right'
#
#     # relationships
#     country = relationship("CountrySchema", back_populates="meta")
#
#     # audit fields
#     created_at = Column(TIMESTAMP, server_default=func.now())
#     updated_at = Column(TIMESTAMP, server_default=func.now(), onupdate=func.now())
#
#     __table_args__ = (
#         CheckConstraint("driving_side IN ('left', 'right')", name="check_driving_side"),
#     )


class CountryLocalizedNameSchema(Base):
    __tablename__ = "country_localized_name"

    id = Column(Integer, primary_key=True)
    country_id = Column(Integer, ForeignKey("country.id", ondelete="CASCADE"))
    language_code = Column(
        Text, nullable=False, index=True
    )  # e.g. 'es', 'es-MX', 'zh-Hant'
    localized_name = Column(Text, nullable=False)  # e.g. 'España', 'México', '中国'

    # audit fields
    created_at = Column(TIMESTAMP, server_default=func.now())
    updated_at = Column(TIMESTAMP, server_default=func.now(), onupdate=func.now())

    country = relationship("CountrySchema", back_populates="localized_names")

    __table_args__ = (
        CheckConstraint(
            "length(language_code) >= 2", name="check_language_code_length"
        ),
    )
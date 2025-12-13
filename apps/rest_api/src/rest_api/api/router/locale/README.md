
> Sample
```json
{
  "locale": "es-MX",
  "language": { "code": "es", "script": "Latn", "direction": "ltr" },
  "region": { "code": "MX", "name_local": "México", "name_global": "Mexico" },

  "fallback_chain": ["es-MX", "es", "root"],

  "field_conventions": {
    "state": {
      "semantic": "administrative_area",
      "regional_term": "estado",
      "required": true,
      "subdivision_type": "state"
    },
    "postal_code": {
      "semantic": "postal_code",
      "format_type": "numeric",
      "pattern": "\\d{5}",
      "example": "01000"
    },
    "city": { "semantic": "city", "required": true },
    "address_line1": { "semantic": "street_address", "required": true },
    "address_line2": { "semantic": "address_unit", "required": false },
    "phone_number": { "semantic": "phone_number", "required": true }
  },

  "address_schema": {
    "lines_order": ["address_line1","address_line2","city","state","postal_code"],
    "uses_subdivisions": true,
    "subdivision_type": "state",
    "postal_position": "after_city"
  },

  "subdivisions": [
    { "code": "CMX", "name_local": "Ciudad de México", "name_global": "Mexico City", "type": "state" }
  ],

  "formatting": {
    "date": { "short": "dd/MM/yyyy", "medium": "d MMM yyyy", "long": "d 'de' MMMM 'de' yyyy", "first_day_of_week": 1 },
    "numbers": { "decimal_separator": ".", "group_separator": ",", "currency_format": "¤#,##0.00", "percent_format": "#,##0 %" },
    "name_order": "given_family"
  },

  "currency": { "code": "MXN", "symbol": "$", "displays_after_amount": false },

  "phone": { "country_code": "+52", "national_example": "55 1234 5678", "international_example": "+52 55 1234 5678" },

  "calendar": { "primary": "gregorian", "alternates": [], "weekend": [6, 0] },

  "examples": {
    "address_format": "Av. Reforma 123, Cuauhtémoc, Ciudad de México, 01000",
    "name_format": "María López",
    "date_format": "25/12/2025"
  },

  "metadata": { "source": "LocaleIQ v1", "last_updated": "2025-01-01T00:00:00Z" }
}
```
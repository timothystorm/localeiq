# Schema Definitions

SQLAlchemy table definitions.

## Medallion Architecture

- Bronze: records claims.
- Silver: records facts.
- Gold: records decisions.

### Bronze

- Bronze rows should never be updated in place.
- Only appended or superseded by new source versions.
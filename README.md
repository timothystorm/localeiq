# LocaleIQ

[![pre-commit](https://img.shields.io/badge/pre--commit-enabled-brightgreen?logo=pre-commit&logoColor=white)](https://pre-commit.com/)

## What will make LocaleIQ top 10%

- 🔥 Treat data as sacred
- 🔥 Implement structured Bronze → Silver → Gold
- 🔥 Define formal public API guarantees
- 🔥 Enforce rigorous, deterministic transformations
- 🔥 Provide provenance for every field
- 🔥 Prioritize correctness over speed early
- 🔥 Version schemas and transformations from the beginning
- 🔥 Maintain strict boundaries between modules
- 🔥 Build consumer trust intentionally and early

## What will kill LocaleIQ if ignored

- 💀 Schema creep
- 💀 Data inaccuracies
- 💀 Hidden mutations in ingestion
- 💀 Lack of deterministic transformations
- 💀 Over-abstracting too early
- 💀 Weak validation pipeline
- 💀 No data provenance
- 💀 Inconsistent API responses over time
- 💀 Poorly handled fallbacks

## API Schema Rules

### API Structure
- nesting depth <= 3
- ays contain objects, never primitives for complex data
-  fields stable once published
- snake_case only

### Meta Block (Required)

```
meta.version
meta.source
meta.provenance_score
meta.timestamp_utc
meta.request_id
```
### Naming
- clear, concise
- abbreviations (except standard ones)
- dynamic keys

### Schema Guarantees
- backward compatibility forever
- breaking changes without new major version
- consistent ordering of keys
- documented nullability

### Error Schema

_Consistent structure:_

```
error.code
error.message
error.status
error.details
error.request_id
```

### Pagination

- cursor-based (recommended)
- consistent across all list endpoints

### Data Correctness

- provenance required for gold layer
- define fallback logic clearly
- deterministic ingestion

### Contracts
- response time SLOs
- freshness guarantees
- deprecation policy
- stability indicators (stable, beta, deprecated)


# LocaleIQ – Foundational Architecture Checklist
*(High-value essentials to build a top-tier platform)*

## 1. **Internal API Contract & Schema Rules**
- Naming conventions  
- Meta block format (version, provenance, request_id, cursor)  
- Pagination rules  
- Error envelope  
- Fallback logic (e.g., locale fallback chain)  
- Stable field/shape guarantees  

---

## 2. **Data Trust / Freshness Specification**
- Freshness layers (bronze/silver/gold)  
- Provenance indicators  
- Confidence or quality score  
- Last_verified timestamps  
- Enrichment sources  

---

## 3. **Observability Foundations**
- request_id generator  
- timing decorator  
- structured JSON logs  
- correlation-id propagation  
- unified error recorder  

---

## 4. **Unified Configuration Layer**
- No module touches `.env` directly  
- Typed config loader (pydantic or attrs)  
- Centralized config validation  
- Config passed as objects, not globals  

---

## 5. **Versioning & Release Strategy**
- Single monorepo version or per-module versioning  
- Semantic versioning rules  
- Tag format (`v0.1.0`)  
- Release flow documented  

---

## 6. **Developer Onboarding Doc**
- [x] make setup / test / lint  
- [ ] module overview  
- [ ] test conventions  
- [ ] folder layout  
- [x] local run instructions  

---

## 7. **Shared Domain Language**
- Canonical definitions for:
  - locale  
  - region  
  - country  
  - currency  
  - datetime  
- Shared domain models or interfaces  
- Prevents semantic drift across modules  

---

## 8. **Coverage Baseline**
- Add coverage config  
- Fail under a low threshold (e.g., 20%)  
- Integrate into CI  

---

## 9. **Strict Import & Dependency Rules**
- Modules import only from `shared`  
- Modules never import each other  
- Enforce via lint + CI  
- Prevent cross-module coupling early  

---

## 10. **Data Lifecycle Documentation**
- bronze → silver → gold model  
- What each layer means  
- Which layers modules can touch  
- How final datasets feed the API  

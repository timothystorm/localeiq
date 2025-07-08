# LocaleIQ API Guidelines

## 🔍 Core API Philosophy

LocaleIQ APIs are designed to be **simple, clear, and task-focused**.

> "Simple data models first. If more data is needed, provide it via a separate API endpoint or via GraphQL."

We intentionally avoid overly nested, bloated, or overly generalized API responses.

## 🔹 Guiding Principles

### 1. **Minimalism By Default**

* Every API response should deliver **only the necessary data** for the specific task.
* Keep payloads flat and predictable.

### 2. **Separation of Concerns**

* Provide additional or advanced data through **separate endpoints**.
* Do **not** overload core APIs with optional metadata, translations, or nested structures.

### 3. **GraphQL for Advanced Needs**

* Complex queries, aggregations, or nested data structures should be addressed via GraphQL endpoints, not REST.
* REST stays optimized for simple lookups and fast data delivery.

### 4. **Consistency Over Cleverness**

* Favor simple, consistent patterns over clever or abstract solutions.
* Prioritize readability and ease of integration for external developers.

### 5. **Versioned Endpoints**

* APIs must be versioned (e.g., `/v1/countries`) to allow future evolution without breaking existing clients.

## 🔹 Examples

**Simple REST Example (Preferred):**

```json
{
  "US": "United States",
  "JP": "Japan"
}
```

**Advanced Data Example:**

* Provide this via a separate endpoint:

```json
{
  "US": {
    "name": "United States",
    "region": "North America",
    "translations": {
      "ja": "アメリカ合衆国"
    }
  }
}
```

**GraphQL Example:**

```graphql
query {
  countries {
    code
    name
    translations(locale: "ja")
  }
}
```

## 🔹 Developer Mantra

> Simple APIs scale better. Clarity always wins over complexity.

LocaleIQ APIs exist to empower developers to **do more with less friction**.

# Project 03 - Data Integration Service

Capstone project. Build a small service that ingests data from an external HTTP API, validates and transforms it, persists the result, and exposes useful data through an API.

This project is intentionally open-ended. There is no reference implementation.

## Scenario

A company has product data in a partner API. Your service must periodically import it into its own database so internal applications can query a stable local representation.

## Required flow

```text
external API
     │
     ▼
HTTP client
     │
     ▼
validation
     │
     ▼
transformation
     │
     ▼
PostgreSQL
     │
     ▼
FastAPI
```

## Minimum requirements

### Ingestion

- fetch paginated data from an HTTP API
- use explicit timeouts
- handle transient failures sensibly
- validate external payloads
- make ingestion safe to run more than once

### Persistence

Store a normalized representation in PostgreSQL.

### API

Expose at least:

```text
GET /products
GET /products/{id}
GET /products?updated_since=...
```

### Operations

Provide a way to trigger an import manually. A scheduled worker is optional.

### Testing

Test transformation and validation without the network. Add at least one integration test covering the ingestion path.

## Suggested milestones

```text
1. fake external API + parser
2. persistence model
3. ingestion service
4. idempotency
5. REST API
6. retries/timeouts
7. async I/O where useful
8. Docker + CI
9. logging/observability
```

## Design questions

Do not answer these by adding abstractions automatically:

- Where should external API models differ from database models?
- Where should retries live?
- How will you detect duplicate imports?
- Which operations benefit from async I/O?
- What should happen if page 7 of 10 fails?
- How will you observe a slow import?

## Definition of done

A developer can start the dependencies locally, configure the external endpoint, run an import, query the imported data, run the test suite, and understand the failure behavior from the logs.

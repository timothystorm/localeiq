# LocaleIQ Data Shared Package

This package contains shared data models, types, and utilities used across multiple LocaleIQ services. It is designed to promote code reuse and maintain consistency in data handling throughout the LocaleIQ ecosystem.

## Build Project `.env` File

Create your local environment configuration from the template:

```bash
   cp .env.local .env
```

Then edit `.env` with your actual database credentials. The `.env` file is git ignored and should never be committed.

## Setup Database

To set up the database for the LocaleIQ Data Shared package, follow these steps:

1. Run `docker compose` to start the database service.
```bash
   docker compose -f docker-compose.local.yml up -d
```
2. Test connection to the database using `psql` or any PostgreSQL client.
```bash
   psql -h localhost -U <DB_USER> -d localeiq
```

> Access PGAdmin at: `http://localhost:8080/`
> PostgresSQL and PGAdmin credentials are found in the .env file. generated above.
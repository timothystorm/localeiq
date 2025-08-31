
## Useful Commands

### Build the Docker Image

> Development

```bash
docker build -t countries-api:dev .
```

> Production

```bash
docker build -t countries-api:prod .
```

### Run the Docker Container

> Development

```bash
docker run --rm \
-p 8080:8080 \
-e ASYNC_DATABASE_URL=postgresql+asyncpg://localeiq:devpassword@host.docker.internal:5432/localeiq \
countries-api:dev
```

### Development cURL Commands

> Get all countries

```bash
curl -X GET "http://localhost:8080/countries" -H "x-locale: fr"
```

# FastAPI Countries API

A simple FastAPI application that provides endpoints for retrieving country information.

## Features

- **Complete Countries List**: Returns 249 countries with ISO country codes and names
- **Country Count**: Get the total number of available countries
- **Automatic API Documentation**: Interactive docs available via Swagger UI
- **Type Hints**: Proper response models for better API documentation

## API Endpoints

### 1. Root Endpoint
- **URL**: `GET /`
- **Description**: Welcome message for the API
- **Response**: `{"message": "Welcome to the Countries API"}`

### 2. Countries List
- **URL**: `GET /countries`
- **Description**: Returns a comprehensive list of all countries
- **Response Format**: Array of objects with `code` and `name` fields
- **Example Response**:
```json
[
  {"code": "AD", "name": "Andorra"},
  {"code": "AE", "name": "United Arab Emirates"},
  {"code": "AF", "name": "Afghanistan"},
  ...
]
```

### 3. Countries Count
- **URL**: `GET /countries/count`
- **Description**: Returns the total number of countries available
- **Response**: `{"total_countries": 249}`

## Running the Application

1. **Activate Virtual Environment**:
   ```bash
   source venv/bin/activate
   ```

2. **Start the Development Server**:
   ```bash
   uvicorn app.main:app --host 0.0.0.0 --port 8000 --reload
   ```

3. **Access the API**:
   - API Base URL: `http://localhost:8000`
   - Interactive Documentation: `http://localhost:8000/docs`
   - Alternative Documentation: `http://localhost:8000/redoc`

## Testing the Endpoints

```bash
# Test root endpoint
curl http://localhost:8000/

# Get all countries
curl http://localhost:8000/countries

# Get countries count
curl http://localhost:8000/countries/count
```

## Project Structure

```
/workspace/
├── app/
│   ├── __init__.py
│   └── main.py          # Main FastAPI application
├── venv/                # Virtual environment
├── pyproject.toml       # Project dependencies
└── README.md
```

## Dependencies

- **FastAPI**: Modern, fast web framework for building APIs
- **Uvicorn**: Lightning-fast ASGI server
- **Python-dotenv**: Environment variable management
- **Pydantic**: Data validation using Python type annotations

The API includes 249 countries with their ISO 3166-1 alpha-2 country codes and official names, making it suitable for use in forms, dropdowns, and other applications requiring country data.
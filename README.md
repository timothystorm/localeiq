# LocaleIQ

> Momentum beats motivation!

## 🛠️  Environment Setup

---
### 🚀 First-Time Setup

Only needs to be done once per machine:

1. **Install Python and set the python version globally:**
   ```bash
   pyenv install 3.14.0
   pyenv global 3.14.0
   ```
   > Python 3.14.0 as of 2025.11.3

2. Install/upgrade pip and runtime dependencies
   ```bash
   python -m pip install --upgrade pip
   ```
   
3. Install poetry
   ```bash
   pip install poetry 
   ```
   
4. Clone project
   ```bash
   git clone git@github.com:timothystorm/localeiq.git
   ```
  
5. Install poetry dependencies
   ```bash
   poetry install
   ```
   
6. (optional) Enter poetry shell
   ```bash
   poetry shell
   ```

---
## 🏃‍♂️‍➡️  Run project

### 🧪 Run tests

```bash
  poetry run test
```

### 🔥 Start application

```bash
  poetry run start
```
---
### 🐳 Start with Docker

#### 📦 Build image
```bash
  docker build -t localeiq:latest .
````

#### 🏃‍♂️ Run container
```bash
  docker run --rm -p 8000:8000 --name localeiq_api localeiq:latest
```

#### 🛑 Stop container
```bash
  docker stop localeiq_api
```

#### Endpoints

- `GET /docs` - Get API docs
- `GET /countries` - Get list of countries
   ```bash
   curl http://localhost:8000/countries
   ```

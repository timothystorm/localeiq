from fastapi import FastAPI

app = FastAPI()


@app.get("/countries")
def list_countries():
    return ["United States", "Canada", "Mexico"]  # placeholder

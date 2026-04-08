from fastapi import FastAPI
from pydantic import BaseModel
from agents import main_agent

app = FastAPI(
    docs_url="/docs",
    redoc_url="/redoc",
    openapi_url="/openapi.json"
)

class Query(BaseModel):
    input: str

@app.get("/")
def home():
    return {"message": "API is running"}

@app.post("/query")
def process_query(query: Query):
    result = main_agent(query.input)

    return {
        "message": " & ".join(result)
    }
from fastapi import FastAPI
from pydantic import BaseModel
from agents import main_agent

app = FastAPI()

class Query(BaseModel):
    input: str

@app.get("/")
def root():
    return {"message": "API is running"}

@app.post("/query")
def process_query(query: Query):
    result = main_agent(query.input)
    return {"message": " & ".join(result)}
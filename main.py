from fastapi import FastAPI
from domain.crew import crew_router
app = FastAPI()

@app.get("/")
def print_hello():
    return "hello"

app.include_router(crew_router.router)
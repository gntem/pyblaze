from unicodedata import name
from fastapi import FastAPI

app = FastAPI(name="pyblaze")

@app.get('/')
def root():
    return ""

@app.get("/health")
def healthcheck():
    return "ok"

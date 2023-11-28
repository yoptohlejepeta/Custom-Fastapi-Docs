from fastapi import FastAPI, Request
from fastapi.templating import Jinja2Templates
from fastapi.staticfiles import StaticFiles

import json
import requests


app = FastAPI(
    title="Fastapi Docs",
)

templates = Jinja2Templates(directory="app/templates")
app.mount("/static", StaticFiles(directory="app/static"), name="static")


@app.get("/")
def index(request: Request):
    response = requests.get("http://127.0.0.1:8000/openapi.json")
    docs_json = json.loads(response.text)

    return templates.TemplateResponse("index.html", {"request": request, "docs": docs_json})
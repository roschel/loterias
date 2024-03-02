from fastapi import FastAPI

from controller.controller import loto_controller
from controller.sort_controller import sort_controller
from database import create_db_and_tables
from fastapi.middleware.cors import CORSMiddleware


app = FastAPI(
    title="API Loteria",
    description="API responsável visualizar jogos da loteria",
    version="0.1.0",
    root_path="",
)

app.include_router(loto_controller, prefix="/loteria", tags=["Loteria"])
app.include_router(sort_controller, prefix="/sorteio", tags=["Sorteador"])

origins = [
    "http://localhost",
    "http://localhost:8080",
    "http://localhost:8081",
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


@app.on_event("startup")
def create_database():
    create_db_and_tables()

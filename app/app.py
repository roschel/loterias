from fastapi import FastAPI

from controller.lotofacil_controller import loto_controller
from controller.sort_controller import sort_controller
from database import create_db_and_tables

app = FastAPI(
    title="API Coupon BKOFFICE",
    description="API responsável por gerenciar cupons criados",
    version="0.1.0",
    root_path="",
)

app.include_router(loto_controller, prefix="/lotofacil", tags=["Lotofácil"])
app.include_router(sort_controller, prefix="/sorteio", tags=["Sorteador"])


@app.on_event("startup")
def create_database():
    create_db_and_tables()

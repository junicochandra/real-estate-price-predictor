from fastapi import APIRouter
from app.adapters.controllers import arithmetic_controller as controller

router = APIRouter(prefix="/arithmetic", tags=["Arithmetic"])

@router.get("/add")
def add(a: int, b: int):
    return controller.add_numbers(a, b)

@router.get("/minus")
def minus(a: int, b: int):
    return controller.subtract_numbers(a, b)

@router.get("/multiply")
def multiply(a: int, b: int):
    return controller.multiply_numbers(a, b)

@router.get("/divide")
def divide(a: int, b: int):
    return controller.divide_numbers(a, b)
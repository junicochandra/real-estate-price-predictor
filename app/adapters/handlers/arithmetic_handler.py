def add_numbers(a: int, b: int):
    return {"result": a + b}


def subtract_numbers(a: int, b: int):
    return {"result": a - b}


def multiply_numbers(a: int, b: int):
    return {"result": a * b}


def divide_numbers(a: int, b: int):
    if b == 0:
        return {"error": "Division by zero is not allowed."}
    return {"result": a / b}

from fastapi import FastAPI
from tests.test_operation import add, sub, mul


chatbot_app = FastAPI(debug=True)

@chatbot_app.post("/add")
async def add_numbers(a: int, b: int):
    result = add(a, b)
    return {"result": result}

@chatbot_app.post("/sub")
async def sub_numbers(a: int, b: int):
    result = sub(a, b)
    return {"result": result}   

@chatbot_app.post("/mul")
async def mul_numbers(a: int, b: int):
    result = mul(a, b)
    return {"result": result}
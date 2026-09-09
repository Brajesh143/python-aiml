import asyncio
from pydantic import BaseModel, Field
from fastapi import FastAPI

app = FastAPI()

class Product(BaseModel):
    name: str
    price: float
    quantity: int


@app.get("/products")
async def get_products():
    await asyncio.sleep(2)
    return [
        Product(name="Product 1", price=10.99, quantity=5),
        Product(name="Product 2", price=19.99, quantity=3),
        Product(name="Product 3", price=5.99, quantity=10),
    ]

# async def get_user():
#     await asyncio.sleep(2)
#     return "user"

# async def get_orders():
#     await asyncio.sleep(2)
#     return "orders"

# async def main():
#     user = await get_user()
#     orders = await get_orders()
#     print(user)
#     print(orders)

# asyncio.run(main())
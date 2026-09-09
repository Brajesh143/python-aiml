import asyncio
from pydantic import BaseModel, Field

async def get_user():
    await asyncio.sleep(2)
    return "user"

async def get_orders():
    await asyncio.sleep(2)
    return "orders"

async def main():
    # sequencial execution
    # user = await get_user()
    # orders = await get_orders()

    # concurrent execution
    
    user, orders = await asyncio.gather(get_user(), get_orders())

    print(user)
    print(orders)

asyncio.run(main())




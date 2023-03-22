import asyncio
import time

from fastapi import APIRouter


router = APIRouter()


async def talk_to_your_friends():
    await asyncio.sleep(2)
    print("Hello how are you?", flush=True)
    print("I'm fine and you", flush=True)

async def chef_making_burger():
    await asyncio.sleep(2)
    print("Burger ready", flush=True)
    return "burger (2x)"

@router.get("/order")
async def order():
    start = time.time()

    order = asyncio.Task(chef_making_burger())
    asyncio.Task(talk_to_your_friends())
    
    order = await order
    return f"Here are your {order}, finish in {time.time() - start:.2f}"
from uuid import uuid4
from typing import Union

from fastapi import APIRouter, HTTPException
from pydantic import BaseModel


router = APIRouter()
orders = {}


class Pizza(BaseModel):
    topping: Union[str, None] = None
    sauce: Union[str, None] = None
    buns: str = None

    class Config:
        schema_extra = {
            "example": 
            {
                "topping": "cheese",
                "sauce": "jalapeno",
                "buns": "large"
            }
        }

class OrderToken(BaseModel):
    order_id: str

    class Config:
        schema_extra = {
            "example":
            {
                "order_id": "<some-random-string>"
            }
        }


@router.post("/order", response_model=OrderToken)
def order(attributes: Pizza):
    order_id = uuid4().hex
    orders[order_id] = attributes
    return OrderToken(order_id=order_id)

@router.get("/{order_id}", response_model=Pizza)
def get_order(order_id: str):
    pizza = orders.get(order_id)
    if pizza:
        return pizza
    return HTTPException(status_code=404, detail="Order not found")
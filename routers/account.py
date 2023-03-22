from fastapi import APIRouter, Form
import jwt
from pydantic import SecretStr


router = APIRouter()


@router.post("/login")
def login(
    username: str = Form(), 
    password: SecretStr = Form()
):
    token = jwt.encode("hello", key="secret_key")
    return "Login Success"
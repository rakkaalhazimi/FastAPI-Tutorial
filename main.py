from fastapi import FastAPI

from routers import pizza, burger, account


app = FastAPI()
app.include_router(account.router, tags=["account"], prefix="/account")
app.include_router(burger.router, tags=["burger"], prefix="/burger")
app.include_router(pizza.router, tags=["pizza"], prefix="/pizza")



@app.get("/")
def index():
    return "Hello world"

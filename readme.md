# FAST API Tutorial

## Installation
1. Install fastapi and uvicorn
   ```
   pip install fastapi uvicorn
   ```

2. Create project in python file
   ```python
   from fastapi import FastAPI

   app = FastAPI()
   
   @app.get("/")
   def index():
    return "Hello world"
   ```

3. Run the server with uvicorn 
   ```
   uvicorn main:app --reload
   ```
   - `main` is the python filename
   - `app` is the FastAPI instance variable name inside python file
   - `--reload` is options to reload the server every file change

4. Visit localhost:8000, port can be different



## Examples
- [Asyncio](routers/burger.py)
- [Account Authentication](routers/account.py)
- [Request Body](routers/pizza.py)
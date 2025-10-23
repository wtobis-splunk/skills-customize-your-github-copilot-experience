# Starter code for FastAPI REST API assignment

from fastapi import FastAPI, HTTPException
from typing import Optional

app = FastAPI()

# Example data store
items = {
    1: {"name": "Apple", "price": 0.99},
    2: {"name": "Banana", "price": 0.59}
}

@app.get("/")
def read_root():
    return {"message": "Welcome to the FastAPI assignment!"}

@app.get("/items/{item_id}")
def read_item(item_id: int):
    item = items.get(item_id)
    if item:
        return item
    raise HTTPException(status_code=404, detail="Item not found")

# (Optional) POST endpoint for adding items
# @app.post("/items/")
# def add_item(item: dict):
#     # Implement item addition logic here
#     pass

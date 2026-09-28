from fastapi import FastAPI, HTTPException
from pydantic import BaseModel

app = FastAPI(title="Task API")


class Item(BaseModel):
    title: str
    description: str = ""


items = []


@app.get("/")
def read_root():
    return {"message": "Welcome to the FastAPI task API!"}


@app.get("/items")
def get_items():
    return items


@app.post("/items")
def create_item(item: Item):
    new_item = {"id": len(items) + 1, **item.model_dump()}
    items.append(new_item)
    return new_item


@app.get("/items/{item_id}")
def get_item(item_id: int):
    for item in items:
        if item["id"] == item_id:
            return item
    raise HTTPException(status_code=404, detail="Item not found")


@app.put("/items/{item_id}")
def update_item(item_id: int, item: Item):
    for index, existing_item in enumerate(items):
        if existing_item["id"] == item_id:
            items[index] = {"id": item_id, **item.model_dump()}
            return items[index]
    raise HTTPException(status_code=404, detail="Item not found")


@app.delete("/items/{item_id}")
def delete_item(item_id: int):
    for index, item in enumerate(items):
        if item["id"] == item_id:
            deleted_item = items.pop(index)
            return {"deleted": deleted_item}
    raise HTTPException(status_code=404, detail="Item not found")

from typing import Dict, Optional

from fastapi import FastAPI, HTTPException, Query
from pydantic import BaseModel, Field

app = FastAPI()

# In-memory storage for items.
items_db: Dict[int, "Item"] = {}
next_id = 1


class Item(BaseModel):
    id: int
    name: str = Field(..., title="Item Name", max_length=100)
    description: Optional[str] = Field(None, title="Optional Description")
    price: float = Field(..., ge=0.0, title="Price (must be non-negative)")


@app.get("/items")
def list_items(min_price: Optional[float] = Query(None, ge=0.0)):
    """Return a list of all items, optionally filtering by minimum price."""
    results = list(items_db.values())
    if min_price is not None:
        results = [item for item in results if item.price >= min_price]
    return results


@app.get("/items/{item_id}")
def get_item(item_id: int):
    """Return a single item by its ID."""
    item = items_db.get(item_id)
    if not item:
        raise HTTPException(status_code=404, detail="Item not found")
    return item


@app.post("/items", status_code=201)
def create_item(item: Item):
    """Create a new item."""
    global next_id

    # Ensure unique IDs for new items
    item.id = next_id
    items_db[next_id] = item
    next_id += 1
    return item


@app.put("/items/{item_id}")
def update_item(item_id: int, item_update: Item):
    """Update an existing item by ID."""
    if item_id not in items_db:
        raise HTTPException(status_code=404, detail="Item not found")

    # Ensure the ID in the payload matches the URL path ID.
    if item_update.id != item_id:
        raise HTTPException(
            status_code=400,
            detail="Item ID in the request body must match the URL path ID.",
        )

    items_db[item_id] = item_update
    return item_update


@app.delete("/items/{item_id}", status_code=204)
def delete_item(item_id: int):
    """Delete an item by ID."""
    if item_id not in items_db:
        raise HTTPException(status_code=404, detail="Item not found")

    del items_db[item_id]
    return None

from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from typing import Dict

app = FastAPI()

# In-memory "space"
db: Dict[str, dict] = {}

# Request models
class Item(BaseModel):
    id: str
    data: dict

class WebhookPayload(BaseModel):
    action: str  # 'add', 'update', 'remove'
    item: Item = None  # For add/update
    id: str = None     # For remove

@app.post("/webhook")
def handle_webhook(payload: WebhookPayload):
    action = payload.action.lower()

    if action == "add":
        if not payload.item:
            raise HTTPException(status_code=400, detail="Missing item for add.")
        if payload.item.id in db:
            raise HTTPException(status_code=400, detail="Item already exists.")
        db[payload.item.id] = payload.item.data
        return {"message": "Item added", "item": payload.item.dict()}

    elif action == "update":
        if not payload.item:
            raise HTTPException(status_code=400, detail="Missing item for update.")
        if payload.item.id not in db:
            raise HTTPException(status_code=404, detail="Item not found.")
        db[payload.item.id] = payload.item.data
        return {"message": "Item updated", "item": payload.item.dict()}

    elif action == "remove":
        if not payload.id:
            raise HTTPException(status_code=400, detail="Missing id for remove.")
        if payload.id not in db:
            raise HTTPException(status_code=404, detail="Item not found.")
        del db[payload.id]
        return {"message": "Item removed", "item_id": payload.id}

    else:
        raise HTTPException(status_code=400, detail="Invalid action. Use add, update, or remove.")


@app.get("/all")
def get_all():
    return db

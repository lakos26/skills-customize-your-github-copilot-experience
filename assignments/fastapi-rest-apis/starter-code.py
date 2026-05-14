from fastapi import FastAPI, HTTPException

app = FastAPI()

items = [
    {"id": 1, "name": "Example item", "description": "A sample record for the API."}
]


@app.get("/")
def read_root():
    return {"message": "Welcome to the FastAPI REST API assignment"}


@app.get("/items")
def read_items():
    return items


@app.post("/items", status_code=201)
def create_item(item: dict):
    name = item.get("name")
    description = item.get("description")

    if not name or not description:
        raise HTTPException(status_code=400, detail="name and description are required")

    new_item = {
        "id": len(items) + 1,
        "name": name,
        "description": description,
    }
    items.append(new_item)
    return new_item
import asyncpg
from fastapi import FastAPI, HTTPException

DATABASE_URL = "postgresql://usrpsgf:AgmIkie2Ijq0@dev-postgres:5432/central_catalog"

app = FastAPI()

@app.on_event("startup")
async def startup():
    app.state.db = await asyncpg.connect(DATABASE_URL)

@app.on_event("shutdown")
async def shutdown():
    await app.state.db.close()

@app.get("/items/{item_id}")
async def read_item(item_id: int):
    item = await app.state.db.fetchrow('SELECT city_code FROM catalog.cities WHERE id=$1', item_id)
    if item is None:
        raise HTTPException(status_code=404, detail="Item not found")
    return item

@app.get("/adress/{item_id}")
async def read_item(item_id: int):
    item = await app.state.db.fetchrow('SELECT adress FROM thesaurus.tree WHERE mid=$1', item_id)
    if item is None:
        raise HTTPException(status_code=404, detail="Item not found")
    return item

# @app.put("/items/{item_id}")
# async def update_item(item_id: int, new_item: str):
#     item = await app.state.db.fetchrow('SELECT * FROM catalog.items WHERE id=$1', item_id)
#     if item is None:
#         raise HTTPException(status_code=404, detail="Item not found")
        
#     await app.state.db.execute('UPDATE catalog.items SET item_name=$1 WHERE id=$2', new_item, item_id)
        
#     return {"message": "Item updated successfully"}
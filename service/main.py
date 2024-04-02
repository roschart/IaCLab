from fastapi import FastAPI, HTTPException
from typing import List
from schemas import Asset

app = FastAPI()
assets: list[Asset] = []


@app.post("/assets/", response_model=Asset)
def create_asset(asset: Asset):
    asset.id = len(assets) + 1
    assets.append(asset)
    return asset


@app.get("/assets/", response_model=List[Asset])
def read_assets():
    return assets


@app.get("/assets/{asset_id}", response_model=Asset)
def read_asset(asset_id: int):
    asset = next((a for a in assets if a.id == asset_id), None)
    if asset is None:
        raise HTTPException(status_code=404, detail="Asset not found")
    return asset


@app.put("/assets/{asset_id}", response_model=Asset)
def update_asset(asset_id: int, asset_update: Asset):
    asset = next((a for a in assets if a.id == asset_id), None)
    if asset is None:
        raise HTTPException(status_code=404, detail="Asset not found")
    asset.value = asset_update.value
    return asset


@app.delete("/assets/{asset_id}", response_model=Asset)
def delete_asset(asset_id: int):
    global assets
    asset = next((a for a in assets if a.id == asset_id), None)
    if asset is None:
        raise HTTPException(status_code=404, detail="Asset not found")
    assets = [a for a in assets if a.id != asset_id]
    return asset

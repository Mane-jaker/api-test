from fastapi import FastAPI
from motor.motor_asyncio import AsyncIOMotorClient

app = FastAPI()

# Conexión a MongoDB
client = AsyncIOMotorClient('mongodb+srv://manebau:zbvqni0m5gYxlM0x@cluster0.hpy3f.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0')
db = client["test_floreria"]

# Incluir rutas
from app.routes import catalog, orders

app.include_router(catalog.router, prefix="/catalog")
app.include_router(orders.router, prefix="/orders")

@app.get("/")
async def root():
    return {"message": "Floreria API"}

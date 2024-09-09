from motor.motor_asyncio import AsyncIOMotorClient
from bson import ObjectId
from app.models import Order, UpdateOrder
from app.main import db

# Crear una nueva orden
async def create_order(order: Order):
    new_order = await db["orders"].insert_one(order.dict())
    return await db["orders"].find_one({"_id": new_order.inserted_id})

# Listar todas las órdenes
async def get_orders():
    orders = await db["orders"].find().to_list(100)
    return orders

# Obtener una orden por ID
async def get_order_by_id(order_id: str):
    if ObjectId.is_valid(order_id):
        return await db["orders"].find_one({"_id": ObjectId(order_id)})
    return None

# Actualizar una orden por ID
async def update_order_by_id(order_id: str, order: UpdateOrder):
    if ObjectId.is_valid(order_id):
        updated_order = await db["orders"].update_one(
            {"_id": ObjectId(order_id)},
            {"$set": order.dict(exclude_unset=True)}
        )
        return updated_order.modified_count > 0
    return False

# Eliminar una orden por ID
async def delete_order_by_id(order_id: str):
    if ObjectId.is_valid(order_id):
        delete_result = await db["orders"].delete_one({"_id": ObjectId(order_id)})
        return delete_result.deleted_count > 0
    return False

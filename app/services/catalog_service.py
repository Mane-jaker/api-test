from motor.motor_asyncio import AsyncIOMotorClient
from bson import ObjectId
from app.models import Product, UpdateProduct
from app.main import db

# Crear un nuevo producto
async def create_product(product: Product):
    new_product = await db["catalog"].insert_one(product.dict())
    return await db["catalog"].find_one({"_id": new_product.inserted_id})

# Listar todos los productos
async def get_products():
    products = await db["catalog"].find().to_list(100)
    return products

# Obtener un producto por ID
async def get_product_by_id(product_id: str):
    if ObjectId.is_valid(product_id):
        return await db["catalog"].find_one({"_id": ObjectId(product_id)})
    return None

# Actualizar un producto por ID
async def update_product_by_id(product_id: str, product: UpdateProduct):
    if ObjectId.is_valid(product_id):
        updated_product = await db["catalog"].update_one(
            {"_id": ObjectId(product_id)},
            {"$set": product.dict(exclude_unset=True)}
        )
        return updated_product.modified_count > 0
    return False

# Eliminar un producto por ID
async def delete_product_by_id(product_id: str):
    if ObjectId.is_valid(product_id):
        delete_result = await db["catalog"].delete_one({"_id": ObjectId(product_id)})
        return delete_result.deleted_count > 0
    return False

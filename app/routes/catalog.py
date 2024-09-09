from fastapi import APIRouter, HTTPException
from app.models import Product, UpdateProduct
from app.services.catalog_service import (
    create_product,
    get_products,
    get_product_by_id,
    update_product_by_id,
    delete_product_by_id
)

router = APIRouter()

# Crear un nuevo producto
@router.post("/")
async def add_product(product: Product):
    return await create_product(product)

# Listar todos los productos
@router.get("/")
async def list_products():
    return await get_products()

# Obtener un producto por ID
@router.get("/{product_id}")
async def get_product(product_id: str):
    product = await get_product_by_id(product_id)
    if not product:
        raise HTTPException(status_code=404, detail="Producto no encontrado")
    return product

# Actualizar un producto por ID
@router.put("/{product_id}")
async def update_product(product_id: str, product: UpdateProduct):
    updated_product = await update_product_by_id(product_id, product)
    if not updated_product:
        raise HTTPException(status_code=404, detail="Producto no encontrado o sin cambios")
    return {"message": "Producto actualizado"}

# Eliminar un producto por ID
@router.delete("/{product_id}")
async def delete_product(product_id: str):
    deleted_product = await delete_product_by_id(product_id)
    if not deleted_product:
        raise HTTPException(status_code=404, detail="Producto no encontrado")
    return {"message": "Producto eliminado"}

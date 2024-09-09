from fastapi import APIRouter, HTTPException
from app.models import Order, UpdateOrder
from app.services.order_service import (
    create_order,
    get_orders,
    get_order_by_id,
    update_order_by_id,
    delete_order_by_id
)

router = APIRouter()

# Crear una nueva orden
@router.post("/")
async def place_order(order: Order):
    return await create_order(order)

# Listar todas las órdenes
@router.get("/")
async def list_orders():
    return await get_orders()

# Obtener una orden por ID
@router.get("/{order_id}")
async def get_order(order_id: str):
    order = await get_order_by_id(order_id)
    if not order:
        raise HTTPException(status_code=404, detail="Orden no encontrada")
    return order

# Actualizar una orden por ID
@router.put("/{order_id}")
async def update_order(order_id: str, order: UpdateOrder):
    updated_order = await update_order_by_id(order_id, order)
    if not updated_order:
        raise HTTPException(status_code=404, detail="Orden no encontrada o sin cambios")
    return {"message": "Orden actualizada"}

# Eliminar una orden por ID
@router.delete("/{order_id}")
async def delete_order(order_id: str):
    deleted_order = await delete_order_by_id(order_id)
    if not deleted_order:
        raise HTTPException(status_code=404, detail="Orden no encontrada")
    return {"message": "Orden eliminada"}

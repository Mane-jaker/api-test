from pydantic import BaseModel
from typing import List, Optional

# Modelo para productos
class Product(BaseModel):
    name: str
    description: Optional[str] = None
    price: float
    stock: int

class UpdateProduct(BaseModel):
    name: Optional[str]
    description: Optional[str]
    price: Optional[float]
    stock: Optional[int]

# Modelo para ítems de una orden
class OrderItem(BaseModel):
    product_id: str
    quantity: int

# Modelo para órdenes
class Order(BaseModel):
    items: List[OrderItem]
    total: float
    customer_name: str
    customer_address: str

class UpdateOrder(BaseModel):
    items: Optional[List[OrderItem]]
    total: Optional[float]
    customer_name: Optional[str]
    customer_address: Optional[str]

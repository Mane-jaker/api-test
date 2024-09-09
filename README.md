## Requisitos

Antes de comenzar, asegúrate de tener instalado lo siguiente:

- **Python 3.12+**

## Instalación

1. **Clona el repositorio**

   ```bash
   git clone https://github.com/Mane-jaker/api-test
   cd api-test

2. **Crea un entorno virtual**

    En sistemas Unix/macOS:

    python3 -m venv venv
    source venv/bin/activate
    
    En Windows:

    python -m venv venv
    venv\Scripts\activate

3. **Instala las dependencias**

    pip install -r requirements.txt

## Ejecución del proyecto

1. Ejecuta el servidor de FastAPI

    uvicorn app.main:app --reload

2. Accede a la documentación de la API

    Swagger: http://127.0.0.1:8000/docs
    Redoc: http://127.0.0.1:8000/redoc

## Estructura del proyecto

    app/
    ├── models.py            # Definición de modelos para Product y Order
    ├── services/
    │   ├── catalog_service.py  # Funciones CRUD para el catálogo
    │   └── order_service.py    # Funciones CRUD para las órdenes
    ├── routes/
    │   ├── catalog.py        # Rutas para el catálogo de productos
    │   └── orders.py         # Rutas para las órdenes
    └── main.py              # Punto de entrada principal

## Endpoints

1. **Catálogo de productos**

    POST /catalog/: Crear un nuevo producto.
    GET /catalog/: Listar todos los productos.
    GET /catalog/{product_id}: Obtener un producto por ID.
    PUT /catalog/{product_id}: Actualizar un producto por ID.
    DELETE /catalog/{product_id}: Eliminar un producto por ID.

2. **Órdenes**

    POST /orders/: Crear una nueva orden.
    GET /orders/: Listar todas las órdenes.
    GET /orders/{order_id}: Obtener una orden por ID.
    PUT /orders/{order_id}: Actualizar una orden por ID.
    DELETE /orders/{order_id}: Eliminar una orden por ID.
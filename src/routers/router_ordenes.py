import peewee
from typing import List, Dict
from functools import reduce
from fastapi import APIRouter, HTTPException, status, Depends
from src.schemas import (
    OrdenSchema, OrdenOutSchema, ProductoSchema,
    OrdenOutListSchema
)
from src.models import Producto, Orden, Usuario
from src.dependencies import oauth2_schema, decode_token_dependency

router = APIRouter(prefix='/ordenes')

@router.get(
    '/{orden_id}', response_model=OrdenOutListSchema,
    dependencies=[Depends(oauth2_schema)]
)
def get_orden_detail(orden_id: int):
    orden = Orden.get_by_id(orden_id)
    productos = orden.productos
    productos_de_orden = list()
    for producto in productos:
        productos_de_orden.append(ProductoSchema(
            nombre_producto=producto.nombre_producto,
            precio_unitario=producto.precio_unitario,
            cantidad=producto.cantidad,
        ))
        
    return OrdenOutListSchema(
        numero_orden=orden.id,
        precio_total=orden.precio_total_orden,
        nombre_cliente=orden.nombre_cliente,
        lista_productos=productos_de_orden,
    )


@router.post(
    '', response_model=OrdenOutSchema,
    response_model_exclude={'lista_productos'},
)
def create_orden(orden: OrdenSchema, user_data: dict = Depends(decode_token_dependency)):
    lista_productos = orden.lista_productos
    lista_productos = [
        producto.model_dump(mode='python')
        for producto in lista_productos
    ]

    # Obtiene la lista de productos existentes y no existentes
    # para tratarlos de forma diferente
    nombre_productos_entrantes = [producto['nombre_producto'] for producto in lista_productos]
    productos_existentes = Producto.select().where(Producto.nombre_producto.in_(nombre_productos_entrantes))
    nombres_productos_existentes = [producto.nombre_producto for producto in productos_existentes]
    productos_no_existentes = [
        producto for producto in lista_productos
        if producto['nombre_producto'] not in nombres_productos_existentes
    ]

    # Crea la orden sin los productos asociados
    usuario = Usuario.get_by_id(user_data['usuario_id'])
    orden = Orden.create(
        usuario=usuario,
        nombre_cliente=orden.nombre_cliente,
        precio_total_orden=reduce(
            lambda x, y: x + y, [producto['precio_unitario'] for producto in lista_productos]),
    )
    
    # Agrega y asocia los productos no existentes en caso
    # de ser necesario
    cantidad_productos = 0
    if productos_no_existentes:
        productos_agregados = Producto.insert_many(productos_no_existentes).returning(Producto)
        orden.productos.add(list(productos_agregados))
        cantidad_productos += len(list(productos_agregados))

    orden.productos.add(list(productos_existentes))
    cantidad_productos += len(list(productos_existentes))
    return OrdenOutSchema(
        numero_orden=orden.id,
        nombre_cliente=orden.nombre_cliente,
        precio_total=orden.precio_total_orden,
        cantidad_productos=cantidad_productos,
    )

from typing import List, Optional
from pydantic import (
    BaseModel, EmailStr, StrictStr, Field,
    SecretStr, NonNegativeFloat, NonNegativeInt
)

class UsuarioSchema(BaseModel):
    email: EmailStr
    nombre: StrictStr
    password: SecretStr


class ProductoSchema(BaseModel):
    nombre_producto: StrictStr
    precio_unitario: NonNegativeFloat
    cantidad: NonNegativeInt = 1


class ProductoInOrdenSchema(ProductoSchema):
    precio_unitario: Optional[NonNegativeFloat] = 0.0


class OrdenSchema(BaseModel):
    nombre_cliente: StrictStr
    lista_productos: List[ProductoInOrdenSchema]


class OrdenOutSchema(OrdenSchema):
    numero_orden: int
    lista_productos: List[ProductoInOrdenSchema] = None
    precio_total: float
    cantidad_productos: int


class OrdenOutListSchema(BaseModel):
    numero_orden: int
    precio_total: float
    nombre_cliente: str
    lista_productos: List[ProductoSchema]

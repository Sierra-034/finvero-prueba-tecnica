from pydantic import (
    BaseModel, EmailStr, StrictStr,
    SecretStr, NonNegativeFloat, NonNegativeInt
)

class UsuarioSchema(BaseModel):
    email: EmailStr
    nombre: StrictStr
    password: SecretStr

class ProductoSchema(BaseModel):
    nombre_producto: StrictStr
    precio_unitario: NonNegativeFloat
    cantidad: NonNegativeInt

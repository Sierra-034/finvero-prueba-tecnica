import bcrypt
from peewee import (
    CharField, FloatField, IntegerField,
    ForeignKeyField, ManyToManyField
)
from src.models.db_conf import BaseModel, psql_db

def create_tables():
    with psql_db:
        psql_db.create_tables([
            Usuario,
            Producto,
            Orden,
            Reporte,
            OrdenProducto,
            ReporteProducto,
        ])

class Usuario(BaseModel):
    email = CharField(unique=True)
    nombre = CharField(max_length=50)
    password = CharField()

    @classmethod
    def authenticate(cls, email, password):
        user_authenticated = cls.get_or_none(
            cls.email == email)

        if not user_authenticated:
            return None
        
        encoded_password = password.encode('utf-8')
        encoded_hasehd_password = user_authenticated.password.encode('utf-8')
        if user_authenticated and bcrypt.checkpw(encoded_password, encoded_hasehd_password):
            return user_authenticated

    @classmethod
    def create_password(cls, password):
        _bytes = password.encode('utf-8')
        return bcrypt.hashpw(_bytes, bcrypt.gensalt(6))


class Producto(BaseModel):
    nombre_producto = CharField(unique=True, max_length=250)
    precio_unitario = FloatField()
    cantidad = IntegerField()


class Orden(BaseModel):
    precio_total_orden = FloatField()
    nombre_cliente = CharField(max_length=200)
    usuario = ForeignKeyField(Usuario, backref='ordenes')
    productos = ManyToManyField(Producto, backref='ordenes')


class Reporte(BaseModel):
    cantidad_productos = IntegerField()
    precio_total = FloatField()
    productos = ManyToManyField(Producto, backref='reportes')


OrdenProducto = Orden.productos.get_through_model()
ReporteProducto = Reporte.productos.get_through_model()

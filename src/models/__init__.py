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

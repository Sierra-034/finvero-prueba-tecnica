from peewee import CharField, FloatField, IntegerField, ForeignKeyField
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
    usuario = ForeignKeyField(Usuario, backref='ordenes')
    nombre_cliente = CharField(max_length=200)
    precio_total_orden = FloatField()


class OrdenProducto(BaseModel):
    orden = ForeignKeyField(Orden, backref='productos_en_orden')
    producto = ForeignKeyField(Producto, backref='ordenes')


class Reporte(BaseModel):
    cantidad_productos = IntegerField()
    precio_total = FloatField()


class ReporteProducto(BaseModel):
    reporte = ForeignKeyField(Reporte, backref='reporte_productos')
    producto = ForeignKeyField(Producto, backref='reportes')

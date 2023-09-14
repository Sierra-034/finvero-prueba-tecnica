from peewee import Model
from playhouse.postgres_ext import PostgresqlDatabase
from src.config import DatabaseSettings

db_settings = DatabaseSettings()

psql_db = PostgresqlDatabase(
    db_settings.database_name,
    user = db_settings.database_user,
    password = db_settings.database_password,
    host = db_settings.database_host,
    port = db_settings.database_port,
)


class BaseModel(Model):
    class Meta:
        pass
        database = psql_db


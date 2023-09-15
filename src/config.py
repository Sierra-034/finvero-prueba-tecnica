from pydantic_settings import BaseSettings

class DatabaseSettings(BaseSettings):
    database_name: str
    database_user: str
    database_password: str
    database_host: str
    database_port: str


class Settings(BaseSettings):
    secret_key: str

from fastapi import FastAPI, APIRouter
from src.models import psql_db, create_tables
from src.routers import (
    productos_router, usuarios_router,
    ordenes_router, authentication_router,
)

app = FastAPI(
    title='Prueba técnica finvero',
    description='Description comming soon',
    version='1.0.0',
)

api_v1 = APIRouter(prefix='/api/v1')
api_v1.include_router(authentication_router)
api_v1.include_router(usuarios_router)
api_v1.include_router(productos_router)
api_v1.include_router(ordenes_router)
app.include_router(api_v1)


@app.on_event('startup')
async def startup_event():
    print('Startup event')
    psql_db.connect(reuse_if_open=True)
    create_tables();


@app.on_event('shutdown')
async def shutdown_event():
    print('Shutdown event')
    psql_db.close()

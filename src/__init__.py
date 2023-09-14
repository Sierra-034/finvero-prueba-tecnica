from fastapi import FastAPI
from src.models import psql_db, create_tables

app = FastAPI(
    title='Prueba técnica finvero',
    description='Description comming soon',
    version='1.0.0',
)

@app.get('/')
def read_root():
    return {'Hello': 'world'}


@app.on_event('startup')
async def startup_event():
    print('Startup event')
    psql_db.connect(reuse_if_open=True)
    create_tables();


@app.on_event('shutdown')
async def shutdown_event():
    print('Shutdown event')
    psql_db.close()

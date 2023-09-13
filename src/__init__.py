from fastapi import FastAPI

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


@app.on_event('shutdown')
async def shutdown_event():
    print('Shutdown event')

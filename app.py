from fastapi import FastAPI
from db import data_base, user2

app = FastAPI()

# Eventos

@app.on_event('startup')
def start():
    if data_base.is_closed():
        data_base.connect()
    data_base.create_tables([user2])

@app.on_event('shutdown')
def shut_down():
    if not data_base.is_closed():
        data_base.close()

# Funciones 

@app.get('/')
async def index():
    return 'hola'

@app.get('/about')
async def about():
    return 'chau'


    
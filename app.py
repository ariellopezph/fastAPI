from http.client import HTTPException
from fastapi import FastAPI
from db import data_base, user2
from schemas import UserRquestModel, UserResponseModel

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

@app.post('/users')
async def crear(user_request: UserRquestModel):
    user = user2.create(
        username = user_request.username,
        email =  user_request.email
    )
    return user_request

@app.get('/users/{user_id}')
async def get_user(user_id):
    user = user2.select().where(user2.id == user_id).first()


    if user:
        return UserResponseModel(id = user.id, username = user.username, email = user.email)
    else:
        return HTTPException(404, "Usuario no encontrado")


@app.delete('/users/{user_id}')
async def delete_user(user_id):
    user = user2.select().where(user2.id == user_id).first()


    if user:
        user.delete_instance()
        return "Usuario eliminado"
    else:
        return HTTPException(404, "Usuario no encontrado")
import peewee
from fastapi import APIRouter, status, HTTPException
from src.schemas import UsuarioSchema, UsuarioOutSchema
from src.models import Usuario

router = APIRouter(prefix='/usuarios')

@router.post(
    '', response_model=UsuarioOutSchema,
    response_model_exclude={'password'},
    status_code=status.HTTP_201_CREATED,
)
def create_usuario(usuario_in: UsuarioSchema):
    try:
        hashed_password = Usuario.create_password(usuario_in.password.get_secret_value())
        usuario_nuevo = Usuario(**usuario_in.model_dump())
        usuario_nuevo.password = hashed_password
        usuario_nuevo.save()
    except peewee.IntegrityError:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail='Error al crear usuario, intente con otros datos',
        )

    return usuario_nuevo


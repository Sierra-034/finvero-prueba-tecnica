import peewee
from fastapi import APIRouter, status
from src.schemas import UsuarioSchema
from src.models import Usuario

router = APIRouter(prefix='/usuarios')

@router.post(
    '', response_model=UsuarioSchema,
    response_model_exclude={'password'},
    status_code=status.HTTP_201_CREATED,
)
def create_usuario(usuario: UsuarioSchema):
    try:
        usuario_nuevo = Usuario.create(**usuario.model_dump())
    except peewee.IntegrityError:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail='Error al crear usuario, intente con otros datos',
        )

    return usuario_nuevo


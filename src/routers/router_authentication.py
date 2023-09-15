from fastapi import APIRouter, Depends, HTTPException, status
from fastapi.security import OAuth2PasswordRequestForm
from src.models import Usuario
from src.common import create_access_token


router = APIRouter(prefix='/auth')

@router.post('')
def auth(data: ... = Depends(OAuth2PasswordRequestForm)):
    user = Usuario.authenticate(data.username, data.password)
    if not user:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail='Los camos [email] o [password] son incorrectos',
            headers={'WWW-Authenticate': 'Bearer'}
        )
    
    return {
        'access_token': create_access_token(user),
        'token_type': 'Bearer',
    }

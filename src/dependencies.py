from fastapi import Depends
from fastapi.security import OAuth2PasswordBearer
from src.common import decode_access_token

oauth2_schema = OAuth2PasswordBearer(tokenUrl='/api/v1/auth')

def decode_token_dependency(token: str = Depends(oauth2_schema)):
    data = decode_access_token(token)
    return data

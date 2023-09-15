import jwt
from datetime import datetime, timedelta
from src.config import Settings


settings = Settings()

def create_access_token(user, expiration_delta=5):
    data = {
        'usuario_id': user.id,
        'usuario_nombre': user.nombre,
        'usuario_email': user.email,
        'exp': datetime.utcnow() + timedelta(minutes=expiration_delta)
    }

    return jwt.encode(data, settings.secret_key, algorithm='HS256')


def decode_access_token(token):
    try:
        return jwt.decode(token, settings.secret_key, algorithms='HS256')
    except Exception:
        return None

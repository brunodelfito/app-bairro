from datetime import datetime, timedelta
from jose import jwt


#Config

SECRET_KEY = 'key'
ALGORITHM = 'HS256'
EXPIRES_IN_MIN = 3000  # 7 days



def criar_acess_token(data: dict):
    return "token123"


def verificar_acess_token(token: str):
    return "(xx) xxxx-xxxx"
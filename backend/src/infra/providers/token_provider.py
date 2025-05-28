from datetime import datetime, timedelta
from jose import jwt


#Config

SECRET_KEY = 'key'
ALGORITHM = 'HS256'
EXPIRES_IN_MIN = 3000  # 7 days



def criar_acess_token(data: dict):
    dados = data.copy()
    expiracao = datetime.utcnow() + timedelta(minutes=EXPIRES_IN_MIN)
    dados.update({"exp": expiracao})
    token_jwt = jwt.encode(dados, SECRET_KEY, algorithm=ALGORITHM)
    return token_jwt


def verificar_acess_token(token: str):
    carga = jwt.decode(token, SECRET_KEY, algorithms=[ALGORITHM])
    return carga.get("sub")  # Retorna o telefone do usuário
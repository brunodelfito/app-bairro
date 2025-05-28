from fastapi import Depends, status, HTTPException
from fastapi.security import OAuth2PasswordBearer
from sqlalchemy.orm import Session
from src.infra.sqlalchemy.config.database import get_db
from src.infra.sqlalchemy.repositorios.repositorio_usuario import RepositorioUsuario
from src.infra.providers import token_provider


oauth2_schema = OAuth2PasswordBearer(tokenUrl='token')


def obter_usuario_logado(token: str = Depends(oauth2_schema)):
    
    try:
        telefone = token_provider.verificar_acess_token(token)
    except Exception as e:
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail="Token inválido ou expirado")
    
    if not telefone:
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail="Token inválido ou expirado")
    
    usuario = RepositorioUsuario(Session).obter_por_telefone(telefone)
    if not usuario:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Usuário não encontrado")    
    
    return usuario
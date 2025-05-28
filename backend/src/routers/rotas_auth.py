from fastapi import APIRouter, status, Depends, HTTPException
from typing import List
from sqlalchemy.orm import Session
from src.schemas.schemas import Usuario, UsuarioSimples, LoginData
from src.infra.sqlalchemy.config.database import get_db
from infra.sqlalchemy.repositorios.repositorio_usuario import RepositorioUsuario
from src.infra.providers import hash_provider, token_provider


router = APIRouter()

#Rotas de usuario
@router.post("/singup", status_code=status.HTTP_201_CREATED, response_model=UsuarioSimples)
def criar_usuario(usuario: Usuario, session: Session = Depends(get_db)):
    usuario.senha = hash_provider.gerar_hash(usuario.senha)
    usuario_criado = RepositorioUsuario(session).criar(usuario)
    return usuario_criado


@router.post("/token", status_code=status.HTTP_200_OK, response_model=UsuarioSimples)
def login(login_data: LoginData, session: Session = Depends(get_db)):
    senha = login_data.senha
    telefone = login_data.telefone

    usuario = RepositorioUsuario(session).obter_por_telefone(telefone)
    if not usuario:
        raise HTTPException(status_code=400, detail="Usuário não encontrado")
    

    senha_valida = hash_provider.verificar_hash(senha, usuario.senha) 
    if not senha_valida:
        raise HTTPException(status_code=400, detail="Senha inválida")
    
    return usuario


@router.get("/usuarios", response_model=list[Usuario]) 
def listar_usuarios(session: Session = Depends(get_db)):
    usuarios = RepositorioUsuario(session).listar()
    return usuarios
from fastapi import FastAPI, Depends, status
from sqlalchemy.orm import Session
from src.schemas.schemas import Produto, Usuario
from src.infra.sqlalchemy.config.database import get_db, criar_bd
from src.infra.sqlalchemy.repositorios.repositorio_produto import RepositorioProduto
from src.infra.sqlalchemy.repositorios.repositorio_usuario import RepositorioUsuario


criar_bd()  # Cria o banco de dados se não existir


app = FastAPI()



#Rotas de produto
@app.post("/produtos")
def criar_produto(produto: Produto, session: Session = Depends(get_db)):
    produto_criado = RepositorioProduto(session).criar(produto)
    return {"msg": "Criado produto"}


@app.get("/produtos")
def listar_produtos(sesion: Session = Depends(get_db)):
    produtos = RepositorioProduto(sesion).listar()
    return produtos

@app.put("/produtos")
def atualizar_produto(produto: Produto, session: Session = Depends(get_db)):
    produto_atualizado = RepositorioProduto(session).editar(produto)
    return {"msg": "Produto atualizado com sucesso", "produto_atualizado": produto_atualizado}


#Rotas de usuario
@app.post("/usuarios", status_code=status.HTTP_201_CREATED, response_model=Usuario)
def criar_usuario(usuario: Usuario, session: Session = Depends(get_db)):
    usuario_criado = RepositorioUsuario(session).criar(usuario)
    return usuario_criado

@app.get("/usuarios", response_model=list[Usuario]) 
def listar_usuarios(session: Session = Depends(get_db)):
    usuarios = RepositorioUsuario(session).listar()
    return usuarios
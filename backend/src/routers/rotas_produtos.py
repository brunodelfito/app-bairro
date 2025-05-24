from fastapi import APIRouter, status, Depends, HTTPException
from typing import List 
from sqlalchemy.orm import Session
from src.infra.sqlalchemy.config.database import get_db
from src.schemas.schemas import Produto
from src.infra.sqlalchemy.repositorios.repositorio_produto import RepositorioProduto

router = APIRouter()


#Rotas de produto
@router.post("/produtos")
def criar_produto(produto: Produto, session: Session = Depends(get_db)):
    produto_criado = RepositorioProduto(session).criar(produto)
    return {"msg": "Criado produto"}


@router.get("/produtos")
def listar_produtos(sesion: Session = Depends(get_db)):
    produtos = RepositorioProduto(sesion).listar()
    return produtos


@router.get("/produtos/{id}")
def exibir_produto(id: int, session: Session = Depends(get_db)):
    produto_localizado = RepositorioProduto(session).buscaPorId(id)
    if not produto_localizado:
        raise HTTPException(status_code=404, detail=f'Produto com id={id}, não encontrado')
    return produto_localizado


@router.put("/produtos/{id}")
def atualizar_produto(id: int, produto: Produto, session: Session = Depends(get_db)):
    produto_atualizado = RepositorioProduto(session).editar(id, produto)
    return {"msg": "Produto atualizado com sucesso", "produto_atualizado": produto_atualizado}


@router.delete("/produtos/{id}")
def remover_produto(id: int, session: Session = Depends(get_db)):
    RepositorioProduto(session).remover(id)
    return {"msg": "Produto removido com sucesso"}
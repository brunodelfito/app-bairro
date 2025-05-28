from fastapi import APIRouter, status, Depends, HTTPException
from typing import List
from sqlalchemy.orm import Session
from src.infra.sqlalchemy.config.database import get_db
from src.infra.sqlalchemy.repositorios.repositorio_pedido import Repositorio_pedido
from src.schemas.schemas import Pedido


router = APIRouter()

@router.post("/pedidos", status_code=status.HTTP_201_CREATED, response_model=Pedido)
def fazer_pedido(pedido: Pedido, session: Session = Depends(get_db)):
    pedido_criado = Repositorio_pedido(session).grava_pedido(pedido)
    return pedido_criado


@router.get("/pedidos/{id}")
def exibir_pedido(id: int, session: Session = Depends(get_db)):
    pedido = Repositorio_pedido(session).obter_por_id(id)
    if not pedido:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Pedido não encontrado")
    return pedido
        

@router.get("/pedidos/", response_model=List[Pedido])
def listar_pedidos(usuario_id: int, session: Session = Depends(get_db)):
    try:
        pedidos = Repositorio_pedido(session).listar_meus_pedidos_por_usuario_id(usuario_id)
        return pedidos
    except:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Nenhum pedido encontrado para o usuário informado.")


@router.get("/pedidos/{usuario_id}/vendas", response_model=List[Pedido])
def listar_vendas(usuario_id: int, session: Session = Depends(get_db)):
    pedidos = Repositorio_pedido(session).listar_minhas_vendas_por_usario_id(usuario_id)
    return pedidos
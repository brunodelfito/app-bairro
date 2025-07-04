from sqlalchemy.orm import Session
from sqlalchemy import update, delete, select
from typing import List
from src.schemas import schemas
from src.infra.sqlalchemy.models import models

class Repositorio_pedido:
    def __init__(self, session: Session) -> None:
        self.session = session

    def grava_pedido(self, pedido: schemas.Pedido) -> models.Pedido:
        pedido_db = models.Pedido(
            quantidade=pedido.quantidade,
            local_entrega=pedido.local_entrega,
            tipo_entrega=pedido.tipo_entrega,
            observacoes=pedido.observacoes,
            usuario_id=pedido.usuario_id,
            produto_id=pedido.produto_id
        )
        self.session.add(pedido_db)
        self.session.commit()
        self.session.refresh(pedido_db)
        return pedido_db

    def obter_por_id(self, id: int) -> models.Pedido:
        query = select(models.Pedido).where(models.Pedido.id == id)
        resultado = self.session.execute(query).one()
        return resultado[0]

    def listar_meus_pedidos_por_usuario_id(self, usuario_id: int) -> List[models.Pedido]:
        pass

    def listar_minhas_vendas_por_usario_id(self, usuario_id: int) -> List[models.Pedido]:
        query = select(models.Pedido) \
            .join_from(models.Pedido, models.Protudo) \
            .where(models.Pedido.usuario_id == usuario_id)
        resultado = self.session.execute(query).scalar.all()
        return resultado
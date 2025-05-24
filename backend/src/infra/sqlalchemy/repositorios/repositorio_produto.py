from sqlalchemy import update, delete, select
from sqlalchemy.orm import Session
from src.schemas import schemas
from src.infra.sqlalchemy.models import models

class RepositorioProduto():

    def __init__(self, session: Session):
        self.session = session

    def criar(self, produto: schemas.Produto):
        db_produto = models.Protudo(nome=produto.nome, detalhes=produto.detalhes, preco=produto.preco, disponivel=produto.disponivel, usuario_id=produto.usuario_id)
        self.session.add(db_produto)
        self.session.commit()
        self.session.refresh(db_produto)
        return db_produto

    def listar(self):
        produtos = self.session.query(models.Protudo).all()
        return produtos
    
    def buscaPorId(self, id: int):
        consulta = select(models.Protudo).where(models.Protudo.id == id)
        produto = self.session.execute(consulta).first()
        return produto

    def editar(self, id: int, produto: schemas.Produto):
        update_stmt = update(models.Protudo).where(models.Protudo.id == id).values(
            nome=produto.nome,
            detalhes=produto.detalhes,
            preco=produto.preco,
            disponivel=produto.disponivel
            )
        
        self.session.execute(update_stmt)
        self.session.commit()
        return produto

    def remover(self, id: int):
        delete_stmt = delete(models.Protudo).where(models.Protudo.id == id)
        self.session.execute(delete_stmt)
        self.session.commit()
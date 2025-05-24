from sqlalchemy import Column, Integer, String, Float, Boolean, ForeignKey
from sqlalchemy.orm import relationship
from src.infra.sqlalchemy.config.database import Base

class Protudo(Base):
    __tablename__ = 'produto'

    id = Column(Integer, primary_key=True, index=True)
    nome = Column(String)
    detalhes = Column(String)
    preco = Column(Float)
    disponivel = Column(Boolean)
    tamanhos = Column(String)
    usuario_id = Column(Integer, ForeignKey('usuario.id'))  # Chave estrangeira para o usuário

    #usuarios_fk = relationship('Usuario', back_populates='produtos_fk')  # Relacionamento com Usuario

    class Config:
        from_attributes = True

class Usuario(Base):
    __tablename__ = 'usuario'

    id = Column(Integer, primary_key=True, index=True)    
    nome = Column(String)
    senha = Column(String)
    telefone = Column(String)

    #produtos_fk = relationship('Produto', back_populates='usuarios_fk')  # Relacionamento com Protudo

    class Config:
        from_attributes = True


class Pedido(Base):
    __tablename__ = 'pedido'

    id = Column(Integer, primary_key=True, index=True)
    quantidade = Column(Integer)
    local_entrega = Column(String)
    tipo_entrega = Column(String)
    observacoes = Column(String, default='Sem observações')

    produto_id = Column(Integer, ForeignKey('produto.id', name='fk_pedido_produto'))  # Chave estrangeira para o produto
    usuario_id = Column(Integer, ForeignKey('usuario.id', name='fk_pedido_usuario'))  # Chave estrangeira para o usuário

    usuario = relationship('Usuario')
    produto = relationship('Protudo')
    


    class Config:
        from_attributes = True
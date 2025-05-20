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
    usuario_id = Column(Integer, ForeignKey('usuario.id', name='fk_nome'))  # Chave estrangeira para o usuário

    usuarios_fk = relationship('usuario', back_populates='produtos_fk')  # Relacionamento com Usuario

class Usuario(Base):
    __tablename__ = 'usuario'

    id = Column(Integer, primary_key=True, index=True)    
    nome = Column(String)
    senha = Column(String)
    telefone = Column(String)

    produtos_fk = relationship('produto', back_populates='usuarios_fk')  # Relacionamento com Protudo
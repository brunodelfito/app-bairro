from pydantic import BaseModel
from typing import Optional, List


class Produto(BaseModel):
    id: Optional[int] = None
    nome: str
    detalhes: str
    preco: float
    disponivel: bool = False
    usuario_id: int
    #usuario: Optional[Usuario]

    class Config:
        from_attributes = True


class Usuario(BaseModel):
    id: Optional[int] = None
    nome: str
    senha: str
    telefone: str
    #meus_produtos: List[Produto] = []
    #minhas_vendas: List[Pedido]
    #meus_pedido: List[Pedido]

    class Config:
        from_attributes = True


class Pedido(BaseModel):
    id: Optional[int] = None
    usuario: Usuario
    produto: Produto
    quantidade: int
    entrega: bool = False
    endereco: str
    observacoes: Optional[str] = 'Sem observações'
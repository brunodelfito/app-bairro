from pydantic import BaseModel
from typing import Optional, List


class Produto(BaseModel):
    id: Optional[int] = None
    nome: str
    detalhes: str
    preco: float
    disponivel: bool = False
    usuario_id: Optional[int]
    #usuario_fk: Optional[Usuario]

    class Config:
        from_attributes = True

class ProdutoSimples(BaseModel):
    id: Optional[int] = None
    nome: str
    detalhes: str
    preco: float
    disponivel: bool = False

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

class UsuarioSimples(BaseModel):
    nome: str
    telefone: str
    #meus_produtos: List[Produto] = []
    #minhas_vendas: List[Pedido]
    #meus_pedido: List[Pedido]

    class Config:
        from_attributes = True

class LoginData(BaseModel):
    senha: str
    telefone: str


    class Config:
        from_attributes = True



class Pedido(BaseModel):
    id: Optional[int] = None
    quantidade: int
    local_entrega: Optional[str]
    tipo_entrega: str
    observacoes: Optional[str] = 'Sem observações'


    usuario_id: Optional[int]
    produto_id: Optional[int]

    class Config:
        from_attributes = True
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from src.infra.sqlalchemy.config.database import criar_bd
from src.routers import rotas_produtos
from src.routers import rotas_usuarios


criar_bd()  # Cria o banco de dados se não existir


app = FastAPI()

origins = ["*", "http://localhost"]  # Permitir todas as origens, ajuste conforme necessário

app.add_middleware(
                    CORSMiddleware,
                    allow_origins=origins,
                    allow_credentials=True,
                    allow_methods=["*"],
                    allow_headers=["*"],
)


#Router

app.include_router(rotas_produtos.router)
app.include_router(rotas_usuarios.router)


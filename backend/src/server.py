from fastapi import FastAPI, Request, BackgroundTasks
from fastapi.middleware.cors import CORSMiddleware
from src.infra.sqlalchemy.config.database import criar_bd
from src.routers import rotas_produtos
from src.routers import rotas_auth
from src.routers import rotas_pedido
from src.jobs import write_notification


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


# Middleware

@app.middleware("http")
async def tempoMiddleware(request: Request, next):
    print('Interceptou chegada')
    response = await next(request)
    print('Interceptou saída') 
    return response





#Router

app.include_router(rotas_produtos.router)
app.include_router(rotas_auth.router, prefix="/auth", tags=["auth"])
app.include_router(rotas_pedido.router)


#Jobs

@app.post("/send-email")
def send_email(email: str, background: BackgroundTasks):
    background.add_task(write_notification, email, 'Ola')
    return {"mgs": "Email enviado com sucesso"}
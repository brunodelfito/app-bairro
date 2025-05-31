
#   Curso

## Video aula:
    https://www.youtube.com/watch?v=Hx6w7JXYHbY&list=PLuhCJtW2i-wKK9HjfYJI4RIcd9AMIi88k&index=1&pp=iAQB

# Executar

python -m src.server
uvicorn src.server:app --reload --reload-dir=src


# Alembic
    alembic init alembic
    
    alembic revision --autogenerate -m "inicial" - Cria uma revisão, faz um depara com anterior se existir, cria as atlterações
    
    alembic upgrade head - Aplicar revisao pendente.


# Requirements
pip install -r requirements.txtscalar_one_or_nonescalar_one_or_none
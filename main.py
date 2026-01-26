from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from backend.routes import auth, users, racha

# Importação das rotas
#from backend.routers import auth, users, properties, geometry, carbon

app = FastAPI(title="RachaAPI ⚽")

API_PREFIX = "/api"

""" --- CONFIGURAÇÃO DO CORS ---
# Permite requisições apenas do frontend autorizado
origins = [
    "http://localhost:5173",
    "http://127.0.0.1:5173",
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)"""

# --- ROTA: HEALTH CHECK ---
# Verifica se a API está online
@app.get("/")
def health_check():
    return {
        "status": "ok",
        "message": "API Racha rodando ⚽"
    }

# --- ROTA: AUTH ---
# Adiciona as rotas de autenticação (login, signup, reset, me)
# URL Final: /api/auth/*
app.include_router(
    auth.router,
    prefix=f"{API_PREFIX}/auth",
    tags=["Auth"]
)


# --- ROTA: USERS ---
# Adiciona as rotas relacionadas aos dados do usuário autenticado
app.include_router(
    users.router,
    prefix=f"{API_PREFIX}/users",
    tags=["Users"]
)


# --- ROTA: RACHAS ---
# Adiciona as rotas de CRUD de RACHAS
app.include_router(
    racha.router,
    prefix=f"{API_PREFIX}/rachas",
    tags=["Rachas"]
)
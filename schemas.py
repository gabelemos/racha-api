from pydantic import BaseModel
from typing import Optional

# --- SCHEMAS PARA O USUARIO ---

class UserLogin(BaseModel):
    email: str
    password: str

class ResetPasswordRequest(BaseModel):
    email: str

class UserSign(BaseModel):
    email: str
    password: str
    nome_completo: str
    
# --- SCHEMAS PARA O RACHA---

class RachaCreate(BaseModel):
    nome: str
    descricao: str
    data_hora: str
    local: str
    formato_jogo: str

class RachaListar(BaseModel):
    id: int

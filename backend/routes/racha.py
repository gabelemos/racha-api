from fastapi import APIRouter, Depends, HTTPException, status
from schemas import RachaCreate, RachaListar
from backend.services.auth_service import get_current_user
from db.supa_connection import get_supabase_client

router = APIRouter()
supabase = get_supabase_client()

@router.get("/")
def listar_rachas(user=Depends(get_current_user)):
    """
    Lista todos os rachas do usuário autenticado.
    """
    response = (
        supabase
        .table("rachas")
        .select("*")
        .eq("owner_id", str(user.id))
        .execute()
    )

    if response.data is None:
        raise HTTPException(status_code=400, detail="Erro ao buscar rachas")

    return response.data

@router.get("/{racha_id}")
def listar_racha_unico(racha_id: int, user=Depends(get_current_user)):
    """
    Lista um racha específico do usuário autenticado.
    """
    response = (
        supabase
        .table("rachas")
        .select("*")
        .eq("owner_id", str(user.id))
        .eq("id", racha_id)
        .execute()
    )

    if not response.data:
        raise HTTPException(status_code=404, detail="Racha não encontrado")

    return response.data

@router.post("/criar")
def create_racha(data: RachaCreate, user=Depends(get_current_user)):
    """
    Cria um novo racha.
    """
    racha_data = {
        "owner_id": user.id,
        "nome": data.nome,
        "descricao": data.descricao,
        "data_hora": data.data_hora,
        "local": data.local,
        "formato_jogo": data.formato_jogo
    }

    print(data)
    
    response = supabase.table("rachas").insert(racha_data).execute()

    if not response.data:
        raise HTTPException(status_code=400, detail="Erro ao criar racha")

    return response.data

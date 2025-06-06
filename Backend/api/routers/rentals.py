from fastapi import APIRouter, HTTPException, status, Depends, Query
from sqlalchemy.orm import Session
from sqlalchemy import select

from schemas import Rental_Schema, Rental_List, Rental_Create_Schema
from models import Rental
from database import get_db

router = APIRouter(prefix="/rentals", tags=["🚗 Aluguéis"])

@router.get("/user", response_model=Rental_List)
async def listar_alugueis_usuario(
    db: Session = Depends(get_db),
    offset: int = Query(0, ge=0),
    limit: int = Query(10, ge=1),
):
    # Aqui removi o filtro por current_user.id, vai listar todos os aluguéis
    query = select(Rental).offset(offset).limit(limit)
    alugueis = db.scalars(query).all()
    return {"rentals": alugueis}

@router.post("/", response_model=Rental_Schema, status_code=status.HTTP_201_CREATED)
async def criar_aluguel(
    aluguel: Rental_Create_Schema,
    db: Session = Depends(get_db),
):
    # Para criar, precisamos que o usuário informe user_id (não mais da autenticação)
    if not aluguel.user_id:
        raise HTTPException(status_code=400, detail="Campo user_id é obrigatório sem autenticação")
    
    novo_aluguel = Rental(
        user_id=aluguel.user_id,  # agora vem do corpo da requisição
        car_id=aluguel.car_id,
        start_date=aluguel.start_date,
        end_date=aluguel.end_date,
    )
    db.add(novo_aluguel)
    db.commit()
    db.refresh(novo_aluguel)
    return novo_aluguel

@router.delete("/{rental_id}", status_code=status.HTTP_204_NO_CONTENT)
async def deletar_aluguel(
    rental_id: int,
    db: Session = Depends(get_db),
):
    aluguel = db.get(Rental, rental_id)
    if not aluguel:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Aluguel não encontrado"
        )
    # Como não temos usuário autenticado, não fazemos verificação de permissão
    db.delete(aluguel)
    db.commit()
    return

##########################################################################################################################
#                             📕 B I B L I O T E C A S       E X T E R N A S                                                                
##########################################################################################################################
from fastapi import APIRouter, Depends, status, HTTPException, Query
from sqlalchemy import select
from sqlalchemy.orm import Session

##########################################################################################################################
#                                            ⬇️ I M P O R T E S                                                     
##########################################################################################################################
from schemas.car import Car_Schema, Car_Create_Schema, Car_List
from database import get_db
from models.cars import Car

router = APIRouter(prefix="/cars", tags=["🚘 Carros"])

##########################################################################################################################
#                                                ✉️ P O S T                                                                
##########################################################################################################################
@router.post("/", response_model=Car_Schema, status_code=status.HTTP_201_CREATED)
async def criar_carro(carro: Car_Create_Schema, db: Session = Depends(get_db)):
    novo_carro = Car(**carro.model_dump())

    db.add(novo_carro)
    db.commit()
    db.refresh(novo_carro)

    return novo_carro

##########################################################################################################################
#                                                  🔍 G E T                                                                   
##########################################################################################################################
@router.get("/", response_model=Car_List)
async def buscar_carros(
    db: Session = Depends(get_db),
    offset: int = Query(0, ge=0),
    limit: int = Query(10, ge=1)
):
    carros = db.scalars(
        select(Car).offset(offset).limit(limit)
    ).all()

    return {"cars": carros}

@router.get("/{car_id}", response_model=Car_Schema)
async def buscar_carro(car_id: int, db: Session = Depends(get_db)):
    carro = db.get(Car, car_id)
    if not carro:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Carro não encontrado!"
        )
    return carro

##########################################################################################################################
#                                                  🔄️ P U T                                                                  
##########################################################################################################################
@router.put("/{car_id}", response_model=Car_Schema)
async def atualizar_carro(
    car_id: int,
    dados: Car_Create_Schema,
    db: Session = Depends(get_db)
):
    carro = db.get(Car, car_id)

    if not carro:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Carro não encontrado!"
        )

    for campo, valor in dados.model_dump().items():
        setattr(carro, campo, valor)

    db.commit()
    db.refresh(carro)

    return carro

##########################################################################################################################
#                                                  🗑️ D E L E T E                                                                 
##########################################################################################################################
@router.delete("/{car_id}", response_model=Car_Schema)
async def excluir_carro(car_id: int, db: Session = Depends(get_db)):
    carro = db.get(Car, car_id)
    if not carro:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Carro não encontrado!"
        )

    db.delete(carro)
    db.commit()

    return carro
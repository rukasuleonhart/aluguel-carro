from http import HTTPStatus

from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from sqlalchemy import select

from schemas import User_Create_Schema, User_Public_Schema
from models import User
from database import get_db

router = APIRouter(prefix="/users", tags=["users"])

@router.post("/", response_model=User_Public_Schema)
def criar_usuario(usuario: User_Create_Schema, db: Session = Depends(get_db)):
    db_user = db.scalar(
        select(User).where((User.email == usuario.email) | (User.telefone == usuario.telefone))
    )
    
    if db_user:
        if db_user.email == usuario.email:
            raise HTTPException(
                status_code=HTTPStatus.CONFLICT, 
                detail="Já existe um cadastro com este email!"
            )
        if db_user.telefone == usuario.telefone:
            raise HTTPException(
                status_code=HTTPStatus.CONFLICT, 
                detail="Já existe um cadastro com este telefone!"
            )

    novo_usuario = User(
        nome=usuario.nome,
        email=usuario.email,
        telefone=usuario.telefone,
    )

    db.add(novo_usuario)
    db.commit()
    db.refresh(novo_usuario)

    return novo_usuario

from http import HTTPStatus
##########################################################################################################################
#                         📕 B I B L I O T E C A S       E X T E R N A S                                                                
##########################################################################################################################
from fastapi import APIRouter, Depends, HTTPException, Query
from sqlalchemy.orm import Session
from sqlalchemy import select

##########################################################################################################################
#                                          ⬇️ I M P O R T E S                                                     
##########################################################################################################################
from schemas import User_Create_Schema, User_Public_Schema, Users_List
from models import User
from database import get_db

router = APIRouter(prefix="/users", tags=["👤 Usuários"])

##########################################################################################################################
#                                             ✉️ P O S T                                                                
##########################################################################################################################
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

##########################################################################################################################
#                                             🔍 G E T                                                                   
##########################################################################################################################
@router.get("/", response_model=Users_List)
def buscar_usuarios(
    db: Session = Depends(get_db),
    offset: int = Query(0, ge=0),
    limit: int = Query(10, ge=1)
):
    listar_usuarios = db.scalars(
        select(User).offset(offset).limit(limit)
    ).all()

    return {"users": listar_usuarios}

##########################################################################################################################
#                                             🔄️ P U T                                                                  
##########################################################################################################################
@router.put("/{user_id}", response_model=User_Public_Schema)
def atualizar_usuario(user_id: int, usuario: User_Create_Schema, db: Session = Depends(get_db)):
    # Verifica se o usuário existe
    db_user = db.get(User, user_id)
    if not db_user:
        raise HTTPException(
            status_code=HTTPStatus.NOT_FOUND,
            detail="Usuário não encontrado!"
        )

    # Verifica se o email ou telefone já estão cadastrados por outro usuário
    db_user_existente = db.scalar(
        select(User).where(
            (User.email == usuario.email) | (User.telefone == usuario.telefone)
        )
    )

    if db_user_existente and db_user_existente.id != user_id:
        if db_user_existente.email == usuario.email:
            raise HTTPException(
                status_code=HTTPStatus.CONFLICT,
                detail="Já existe um cadastro com este email!"
            )
        if db_user_existente.telefone == usuario.telefone:
            raise HTTPException(
                status_code=HTTPStatus.CONFLICT,
                detail="Já existe um cadastro com este telefone!"
            )

    # Atualiza os dados do usuário
    db_user.nome = usuario.nome
    db_user.email = usuario.email
    db_user.telefone = usuario.telefone

    db.commit()
    db.refresh(db_user)

    return db_user

##########################################################################################################################
#                                            🗑️ Delete                                                                 
##########################################################################################################################
@router.delete("/{user_id}", response_model=User_Public_Schema)
def excluir_usuario(user_id: int, db: Session = Depends(get_db)):
    # Verifica se o usuário existe
    db_user = db.get(User, user_id)
    if not db_user:
        raise HTTPException(
            status_code=HTTPStatus.NOT_FOUND,
            detail="Usuário não encontrado!"
        )
 
    # Exclui o usuário
    db.delete(db_user)
    db.commit()

    return db_user
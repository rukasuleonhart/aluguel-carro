##########################################################################################################################
#                             📕 B I B L I O T E C A S       E X T E R N A S                                                                
##########################################################################################################################
from fastapi import APIRouter, HTTPException, status, Query, Depends
from sqlalchemy.orm import Session
from sqlalchemy import select
from sqlalchemy.exc import IntegrityError

##########################################################################################################################
#                                            ⬇️ I M P O R T E S                                                     
##########################################################################################################################
from schemas.user import User_Create_Schema, User_Public_Schema, Users_List
from models import User
from database import get_db
from security import get_password_hash, get_current_user

router = APIRouter(prefix="/users", tags=["👤 Usuários"])

##########################################################################################################################
#                                                ✉️ P O S T                                                                
##########################################################################################################################
@router.post("/", response_model=User_Public_Schema, status_code=status.HTTP_201_CREATED)
async def criar_usuario(usuario: User_Create_Schema, db: Session = Depends(get_db)):
    db_user = db.scalar(
        select(User).where((User.email == usuario.email) | (User.telefone == usuario.telefone))
    )
    
    if db_user:
        if db_user.email == usuario.email:
            raise HTTPException(
                status_code=status.HTTP_409_CONFLICT, 
                detail="Já existe um cadastro com este email!"
            )
        if db_user.telefone == usuario.telefone:
            raise HTTPException(
                status_code=status.HTTP_409_CONFLICT, 
                detail="Já existe um cadastro com este telefone!"
            )

    novo_usuario = User(
        nome=usuario.nome,
        email=usuario.email,
        telefone=usuario.telefone,
        senha=get_password_hash(usuario.senha),
    )

    db.add(novo_usuario)
    db.commit()
    db.refresh(novo_usuario)

    return novo_usuario

##########################################################################################################################
#                                                  🔍 G E T                                                                   
##########################################################################################################################
@router.get("/", response_model=Users_List)
async def buscar_usuarios(
    db: Session = Depends(get_db),
    offset: int = Query(0, ge=0),
    limit: int = Query(10, ge=1),
):
    listar_usuarios = db.scalars(
        select(User).offset(offset).limit(limit)
    ).all()

    return {"users": listar_usuarios}

@router.get("/{user_id}", response_model=User_Public_Schema)
async def buscar_usuario(user_id: int, db: Session = Depends(get_db)):
    usuario = db.query(User).filter(User.id == user_id).first()
    if usuario is None:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Usuário não encontrado!"
        )
    return usuario

##########################################################################################################################
#                                                  🔄️ P U T                                                                  
##########################################################################################################################
@router.put("/{user_id}", response_model=User_Public_Schema)
async def atualizar_usuario(
    user_id: int, 
    usuario: User_Create_Schema, 
    db: Session = Depends(get_db),
):
    db_user = db.get(User, user_id)
    if not db_user:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Usuário não encontrado!"
        )
    try:
        db_user.nome = usuario.nome
        db_user.email = usuario.email
        db_user.telefone = usuario.telefone
        db_user.senha = get_password_hash(usuario.senha)

        db.commit()
        db.refresh(db_user)

        return db_user
    except IntegrityError:
        raise HTTPException(
            detail="Este email já existe",
            status_code=status.HTTP_409_CONFLICT
        )

##########################################################################################################################
#                                                  🗑️ Delete                                                                 
##########################################################################################################################
@router.delete("/{user_id}", response_model=User_Public_Schema)
async def excluir_usuario(user_id: int, db: Session = Depends(get_db)):
    db_user = db.get(User, user_id)
    if not db_user:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Usuário não encontrado!"
        )

    db.delete(db_user)
    db.commit()

    return db_user
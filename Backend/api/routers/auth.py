from fastapi import APIRouter, Depends, HTTPException, status
from fastapi.security import OAuth2PasswordRequestForm
from sqlalchemy.orm import Session
from sqlalchemy import select
from database import get_db
from models import User
from security import verify_password, create_access_token
from schemas import Token_Schema

router = APIRouter(prefix="/token", tags=["🔐 Autenticação"])

@router.post("/", response_model=Token_Schema)
def gerar_token_de_acesso(
    form_data: OAuth2PasswordRequestForm = Depends(),
    session: Session = Depends(get_db),
):
    # OAuth2PasswordRequestForm usa 'username', mas aqui ele representa o email
    user = session.scalar(select(User).where(User.email == form_data.username))

    if not user or not verify_password(form_data.password, user.senha):
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="email ou senha incorreto!",
            headers={"WWW-Authenticate": "Bearer"},
        )
    
    access_token = create_access_token({"sub": user.email})

    return Token_Schema(access_token=access_token, token_type="Bearer")

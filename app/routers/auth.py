# routers/auth.py
from fastapi import APIRouter, Depends, HTTPException, status
from fastapi.security import OAuth2PasswordRequestForm
from sqlalchemy.orm import Session
from sqlalchemy.exc import IntegrityError

from datab import get_db
from models.user import Usuario
from schemas.user_schema import UsuarioCreate, UsuarioResponse, Token
from core.security import hash_password, verify_password, create_access_token

router = APIRouter()


@router.post("/register", response_model=UsuarioResponse, status_code=status.HTTP_201_CREATED)
def registrar_usuario(usuario: UsuarioCreate, db: Session = Depends(get_db)):
    nuevo_usuario = Usuario(
        nombre_empresa=usuario.nombre_empresa,
        cif_nif=usuario.cif_nif,
        email=usuario.email,
        password_hash=hash_password(usuario.password),
        rol=usuario.rol,
        telefono=usuario.telefono,
        direccion=usuario.direccion,
    )

    db.add(nuevo_usuario)
    try:
        db.commit()
        db.refresh(nuevo_usuario)
    except IntegrityError:
        db.rollback()
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="El email o CIF/NIF ya está registrado"
        )

    return nuevo_usuario


@router.post("/login", response_model=Token)
def iniciar_sesion(form_data: OAuth2PasswordRequestForm = Depends(), db: Session = Depends(get_db)):
    usuario = db.query(Usuario).filter(Usuario.email == form_data.username).first()

    if not usuario or not verify_password(form_data.password, usuario.password_hash):
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Email o contraseña incorrectos",
            headers={"WWW-Authenticate": "Bearer"},
        )

    access_token = create_access_token(data={"sub": str(usuario.id), "rol": usuario.rol})

    return {"access_token": access_token, "token_type": "bearer"}
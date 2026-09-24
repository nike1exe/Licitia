# schemas/user_schema.py
from pydantic import BaseModel, EmailStr
from datetime import datetime
from typing import Optional

class UsuarioCreate(BaseModel):
    nombre_empresa: str
    cif_nif: str
    email: EmailStr
    password: str
    rol: str  # "cliente" o "proveedor"
    telefono: Optional[str] = None
    direccion: Optional[str] = None

class UsuarioLogin(BaseModel):
    email: EmailStr
    password: str

class UsuarioResponse(BaseModel):
    id: int
    nombre_empresa: str
    cif_nif: str
    email: EmailStr
    rol: str
    telefono: Optional[str] = None
    direccion: Optional[str] = None
    activo: bool
    fecha_registro: datetime

    class Config:
        from_attributes = True  # permite convertir desde el modelo SQLAlchemy

class Token(BaseModel):
    access_token: str
    token_type: str = "bearer"
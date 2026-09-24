# schemas/tarjeta_schema.py
from pydantic import BaseModel
from datetime import datetime
from typing import Optional

class TarjetaCreate(BaseModel):
    titulo: str
    descripcion_original: str
    categoria: Optional[str] = None
    presupuesto_estimado: Optional[float] = None
    fecha_limite: Optional[datetime] = None

class TarjetaResponse(BaseModel):
    id: int
    cliente_id: int
    titulo: str
    descripcion_original: str
    ficha_generada: Optional[str] = None
    categoria: Optional[str] = None
    presupuesto_estimado: Optional[float] = None
    estado: str
    fecha_creacion: datetime
    fecha_limite: Optional[datetime] = None

    class Config:
        from_attributes = True
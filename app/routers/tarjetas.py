# routers/tarjetas.py
from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session
from typing import List

from datab import get_db
from models.tarjeta import Tarjeta
from models.user import Usuario
from schemas.tarjeta_schema import TarjetaCreate, TarjetaResponse
from core.security import get_current_user

router = APIRouter()


@router.post("/", response_model=TarjetaResponse, status_code=status.HTTP_201_CREATED)
def crear_tarjeta(
    tarjeta: TarjetaCreate,
    db: Session = Depends(get_db),
    current_user: Usuario = Depends(get_current_user)
):
    if current_user.rol != "cliente":
        raise HTTPException(
            status_code=status.HTTP_403_FORBIDDEN,
            detail="Solo los clientes pueden crear tarjetas técnicas"
        )

    nueva_tarjeta = Tarjeta(
        cliente_id=current_user.id,
        titulo=tarjeta.titulo,
        descripcion_original=tarjeta.descripcion_original,
        categoria=tarjeta.categoria,
        presupuesto_estimado=tarjeta.presupuesto_estimado,
        fecha_limite=tarjeta.fecha_limite,
    )

    db.add(nueva_tarjeta)
    db.commit()
    db.refresh(nueva_tarjeta)

    return nueva_tarjeta


@router.get("/", response_model=List[TarjetaResponse])
def listar_tarjetas(
    db: Session = Depends(get_db),
    current_user: Usuario = Depends(get_current_user)
):
    if current_user.rol == "cliente":
        # el cliente ve solo sus propias tarjetas
        return db.query(Tarjeta).filter(Tarjeta.cliente_id == current_user.id).all()
    else:
        # el proveedor ve todas las tarjetas abiertas
        return db.query(Tarjeta).filter(Tarjeta.estado == "abierta").all()


@router.get("/{tarjeta_id}", response_model=TarjetaResponse)
def obtener_tarjeta(
    tarjeta_id: int,
    db: Session = Depends(get_db),
    current_user: Usuario = Depends(get_current_user)
):
    tarjeta = db.query(Tarjeta).filter(Tarjeta.id == tarjeta_id).first()
    if not tarjeta:
        raise HTTPException(status_code=404, detail="Tarjeta no encontrada")
    return tarjeta
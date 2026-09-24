# models/user.py
from sqlalchemy import Column, Integer, String, DateTime, Boolean
from sqlalchemy.orm import relationship
from datetime import datetime
from datab import Base

class Usuario(Base):
    __tablename__ = "usuarios"

    id = Column(Integer, primary_key=True, index=True)
    nombre_empresa = Column(String(255), nullable=False)
    cif_nif = Column(String(20), unique=True, nullable=False)
    email = Column(String(255), unique=True, nullable=False, index=True)
    password_hash = Column(String(255), nullable=False)
    rol = Column(String(50), nullable=False)  # "cliente" o "proveedor"
    telefono = Column(String(20), nullable=True)
    direccion = Column(String(500), nullable=True)
    activo = Column(Boolean, default=True)
    fecha_registro = Column(DateTime, default=datetime.utcnow)

    tarjetas = relationship("Tarjeta", back_populates="cliente")
    propuestas = relationship("Propuesta", back_populates="proveedor")
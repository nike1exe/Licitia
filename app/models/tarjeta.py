# models/tarjeta.py
from sqlalchemy import Column, Integer, String, Text, ForeignKey, DateTime, Float
from sqlalchemy.orm import relationship
from datetime import datetime
from datab import Base

class Tarjeta(Base):
    __tablename__ = "tarjetas_tecnicas"

    id = Column(Integer, primary_key=True, index=True)
    cliente_id = Column(Integer, ForeignKey("usuarios.id"), nullable=False)
    titulo = Column(String(255), nullable=False)
    descripcion_original = Column(Text, nullable=False)      # texto que escribió el usuario
    ficha_generada = Column(Text, nullable=True)               # resultado estructurado de la IA
    categoria = Column(String(100), nullable=True)
    presupuesto_estimado = Column(Float, nullable=True)
    estado = Column(String(50), default="abierta")              # abierta, en_evaluacion, cerrada
    fecha_creacion = Column(DateTime, default=datetime.utcnow)
    fecha_limite = Column(DateTime, nullable=True)

    cliente = relationship("Usuario", back_populates="tarjetas")
    propuestas = relationship("Propuesta", back_populates="tarjeta")
# models/propuesta.py
from sqlalchemy import Column, Integer, String, Float, ForeignKey, DateTime, Boolean, Text
from sqlalchemy.orm import relationship
from datetime import datetime
from datab import Base

class Propuesta(Base):
    __tablename__ = "propuestas"

    id = Column(Integer, primary_key=True, index=True)
    tarjeta_id = Column(Integer, ForeignKey("tarjetas_tecnicas.id"), nullable=False)
    proveedor_id = Column(Integer, ForeignKey("usuarios.id"), nullable=False)
    precio_ofertado = Column(Float, nullable=False)
    descripcion = Column(Text, nullable=True)
    es_anomala = Column(Boolean, default=False)
    motivo_anomalia = Column(String(255), nullable=True)
    estado = Column(String(50), default="pendiente")   # pendiente, aceptada, rechazada
    fecha_envio = Column(DateTime, default=datetime.utcnow)

    tarjeta = relationship("Tarjeta", back_populates="propuestas")
    proveedor = relationship("Usuario", back_populates="propuestas")
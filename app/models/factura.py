# models/factura.py
from sqlalchemy import Column, Integer, String, Float, ForeignKey, DateTime
from sqlalchemy.orm import relationship
from datetime import datetime
from datab import Base

class Factura(Base):
    __tablename__ = "facturas"

    id = Column(Integer, primary_key=True, index=True)
    propuesta_id = Column(Integer, ForeignKey("propuestas.id"), nullable=False)
    numero_factura = Column(String(50), unique=True, nullable=False)   # requerido por Veri*factu
    cif_emisor = Column(String(20), nullable=False)
    cif_receptor = Column(String(20), nullable=False)
    base_imponible = Column(Float, nullable=False)
    tipo_iva = Column(Float, default=21.0)                              # 21% estándar España
    cuota_iva = Column(Float, nullable=False)
    total = Column(Float, nullable=False)
    ruta_pdf_s3 = Column(String(500), nullable=True)                     # ubicación del PDF en S3
    fecha_emision = Column(DateTime, default=datetime.utcnow)

    propuesta = relationship("Propuesta")
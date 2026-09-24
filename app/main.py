# main.py
from fastapi import FastAPI
from routers import auth, tarjetas
from models import user, tarjeta, propuesta, factura

app = FastAPI(
    title="LicitIA API",
    description="API REST para la plataforma de licitaciones B2B con IA",
    version="1.0.0"
)

app.include_router(auth.router, prefix="/auth", tags=["Autenticación"])
app.include_router(tarjetas.router, prefix="/tarjetas", tags=["Tarjetas Técnicas"])

@app.get("/")
def root():
    return {"status": "LicitIA API activa"}
from dotenv import load_dotenv
load_dotenv()  # deve ser chamado ANTES de qualquer import que leia os.getenv

from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from .routers import steam, diagnose

app = FastAPI(
    title="Dr. K. Psicólogo Gamer API",
    description="Diagnósticos psicológicos fictícios baseados em perfis Steam",
    version="1.0.0",
)

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["GET", "POST"],
    allow_headers=["*"],
)

app.include_router(steam.router)
app.include_router(diagnose.router)


@app.get("/health")
def health():
    return {"status": "ok"}

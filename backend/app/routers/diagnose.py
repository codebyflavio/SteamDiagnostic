from fastapi import APIRouter
from pydantic import BaseModel, field_validator
from ..diagnosis.engine import generate_diagnosis

router = APIRouter(prefix="/diagnose", tags=["diagnose"])


class GameItem(BaseModel):
    name: str = ""
    playtime_forever: int = 0
    appid: int = 0

    @field_validator("name")
    @classmethod
    def sanitize_name(cls, v: str) -> str:
        return v.strip()[:200]  # limita tamanho do nome


class DiagnoseRequest(BaseModel):
    username: str = "Anônimo"
    games: list[GameItem] = []

    @field_validator("username")
    @classmethod
    def sanitize_username(cls, v: str) -> str:
        return v.strip()[:100] or "Anônimo"

    @field_validator("games")
    @classmethod
    def limit_games(cls, v: list[GameItem]) -> list[GameItem]:
        return v[:2000]  # previne payloads absurdos


@router.post("")
async def diagnose(body: DiagnoseRequest):
    games_dicts = [g.model_dump() for g in body.games]
    result = generate_diagnosis(games=games_dicts, username=body.username)
    return result

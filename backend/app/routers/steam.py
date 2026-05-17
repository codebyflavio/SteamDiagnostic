import asyncio
import os
import httpx
from fastapi import APIRouter, HTTPException

router = APIRouter(prefix="/steam", tags=["steam"])

STEAM_API_BASE = "https://api.steampowered.com"
_TIMEOUT = httpx.Timeout(10.0, connect=5.0)


def _get_key() -> str:
    key = os.getenv("STEAM_API_KEY", "")
    if not key:
        raise HTTPException(status_code=500, detail="STEAM_API_KEY não configurada.")
    return key


def _is_steam_id64(value: str) -> bool:
    """SteamID64 é um número de 17 dígitos começando com 7656119."""
    return value.isdigit() and 15 <= len(value) <= 20


async def _vanity_to_steamid(vanity: str, client: httpx.AsyncClient) -> str:
    try:
        resp = await client.get(
            f"{STEAM_API_BASE}/ISteamUser/ResolveVanityURL/v1/",
            params={"key": _get_key(), "vanityurl": vanity},
        )
        resp.raise_for_status()
    except httpx.HTTPStatusError as e:
        raise HTTPException(status_code=502, detail=f"Erro ao consultar Steam API: {e.response.status_code}")
    except httpx.RequestError:
        raise HTTPException(status_code=504, detail="Steam API não respondeu. Tente novamente.")

    data = resp.json().get("response", {})
    if data.get("success") != 1:
        raise HTTPException(status_code=404, detail="Perfil Steam não encontrado. Verifique se o nome está correto.")
    return data["steamid"]


async def _get_player_summary(steam_id: str, client: httpx.AsyncClient) -> dict:
    try:
        resp = await client.get(
            f"{STEAM_API_BASE}/ISteamUser/GetPlayerSummaries/v2/",
            params={"key": _get_key(), "steamids": steam_id},
        )
        resp.raise_for_status()
    except httpx.HTTPStatusError as e:
        raise HTTPException(status_code=502, detail=f"Erro ao buscar perfil: {e.response.status_code}")
    except httpx.RequestError:
        raise HTTPException(status_code=504, detail="Steam API não respondeu.")

    players = resp.json().get("response", {}).get("players", [])
    if not players:
        raise HTTPException(status_code=404, detail="Perfil Steam não encontrado ou é privado.")
    return players[0]


async def _get_owned_games(steam_id: str, client: httpx.AsyncClient) -> list[dict]:
    try:
        resp = await client.get(
            f"{STEAM_API_BASE}/IPlayerService/GetOwnedGames/v1/",
            params={
                "key": _get_key(),
                "steamid": steam_id,
                "include_appinfo": True,
                "include_played_free_games": True,
            },
        )
        resp.raise_for_status()
    except httpx.HTTPStatusError as e:
        raise HTTPException(status_code=502, detail=f"Erro ao buscar jogos: {e.response.status_code}")
    except httpx.RequestError:
        raise HTTPException(status_code=504, detail="Steam API não respondeu.")

    return resp.json().get("response", {}).get("games", [])


@router.get("/{identifier}")
async def get_steam_profile(identifier: str):
    """
    Retorna perfil + lista de jogos de um usuário Steam.
    Aceita SteamID64 numérico ou vanity URL (nome customizado).
    """
    identifier = identifier.strip()
    if not identifier or len(identifier) > 100:
        raise HTTPException(status_code=400, detail="Identificador inválido.")

    async with httpx.AsyncClient(timeout=_TIMEOUT) as client:
        steam_id = identifier if _is_steam_id64(identifier) else await _vanity_to_steamid(identifier, client)

        summary, games = await asyncio.gather(
            _get_player_summary(steam_id, client),
            _get_owned_games(steam_id, client),
        )

    return {
        "steam_id": steam_id,
        "username": summary.get("personaname", "Anônimo"),
        "avatar": summary.get("avatarfull", ""),
        "profile_url": summary.get("profileurl", ""),
        "games": games,
        "total_games": len(games),
    }

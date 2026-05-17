"""
Motor de diagnóstico: recebe lista de jogos, detecta padrões,
mistura blocos e retorna o diagnóstico final.
"""

import random
from .categorizer import categorize_games, get_dominant_categories
from .blocks.symptoms import SYMPTOMS, SPECIAL_SYMPTOMS
from .blocks.cid_names import CID_NAMES, HYBRID_SUFFIXES
from .blocks.prognosis import PROGNOSIS, SPECIAL_PROGNOSIS
from .blocks.remedies import REMEDIES


BACKLOG_CEMETERY_MIN_GAMES = 50
BACKLOG_CEMETERY_MAX_PLAYED = 0.1
HIGH_HOURS_THRESHOLD = 500
LOW_HOURS_THRESHOLD = 2
DIVERSE_CATEGORIES_THRESHOLD = 6


def _minutes_to_hours(minutes: int) -> float:
    return round(minutes / 60, 1)


def _detect_special_conditions(games: list[dict]) -> list[str]:
    flags: list[str] = []
    total = len(games)
    if total == 0:
        return flags

    unique_names = {g.get("name", "") for g in games}
    if len(unique_names) == 1:
        flags.append("mono_library")
        return flags

    if total >= BACKLOG_CEMETERY_MIN_GAMES:
        with_time = sum(1 for g in games if g.get("playtime_forever", 0) > 30)
        if with_time / total < BACKLOG_CEMETERY_MAX_PLAYED:
            flags.append("backlog_cemetery")

    for game in games:
        if _minutes_to_hours(game.get("playtime_forever", 0)) >= HIGH_HOURS_THRESHOLD:
            flags.append("high_hours")
            break

    for game in games:
        hours = _minutes_to_hours(game.get("playtime_forever", 0))
        if 0 < hours < LOW_HOURS_THRESHOLD:
            flags.append("low_hours")
            break

    return flags


def _build_cid(categories: list[str]) -> str:
    if not categories:
        return "TGI-NE — Transtorno Gamer Indefinido (Não Especificado)"
    if len(categories) == 1:
        options = CID_NAMES.get(categories[0])
        if options:
            return random.choice(options)
        return "TGI — Transtorno Gamer Indefinido"
    suffixes = [HYBRID_SUFFIXES.get(cat, cat.title()) for cat in categories[:2]]
    return f"TPGH — Transtorno de Personalidade Gamer Híbrido ({' + '.join(suffixes)})"


def _pick_unique_symptoms(categories: list[str], exclude: set[str], count: int) -> list[str]:
    """
    Seleciona sintomas únicos intercalando entre categorias dominantes.
    Shuffle por categoria garante variedade entre runs.
    """
    # Cria pools embaralhados por categoria
    cat_pools: list[list[str]] = []
    for cat in categories:
        pool = [s for s in SYMPTOMS.get(cat, []) if s not in exclude]
        if pool:
            random.shuffle(pool)
            cat_pools.append(pool)

    # Intercala: 1 de cada categoria até completar `count`
    picked: list[str] = []
    i = 0
    while len(picked) < count and any(cat_pools):
        for pool in cat_pools:
            if len(picked) >= count:
                break
            if i < len(pool):
                picked.append(pool[i])
        i += 1
        # Remove pools esgotados
        cat_pools = [p for p in cat_pools if i < len(p)]

    return picked[:count]


def generate_diagnosis(games: list[dict], username: str = "Anônimo") -> dict:
    if not games:
        return {
            "patient": username,
            "cid": "TGI-NE — Transtorno Gamer Indefinido (Biblioteca Vazia)",
            "symptoms": ["Biblioteca Steam vazia — o verdadeiro transtorno começa aqui"],
            "prognosis": "Prognóstico: compre um jogo. Qualquer um. Não importa qual.",
            "remedy": "Prescrição: abra a Steam Store. O Dr. K. não pode te ajudar sem dados.",
            "dominant_categories": [],
            "special_flags": ["empty_library"],
            "total_games": 0,
        }

    total_games = len(games)
    special_flags = _detect_special_conditions(games)
    categorized = categorize_games(games)
    dominant_cats = get_dominant_categories(categorized, top_n=3)
    distinct_cat_count = len([k for k in categorized if k != "outros"])
    is_diverse = distinct_cat_count >= DIVERSE_CATEGORIES_THRESHOLD

    # --- CID ---
    if "mono_library" in special_flags:
        cid = "MVU — Monogamia Virtual Urgente"
    elif dominant_cats:
        cid = _build_cid(dominant_cats)
    else:
        cid = "TGI-NE — Transtorno Gamer Indefinido (Não Especificado)"

    # --- Sintomas ---
    used: set[str] = set()
    symptoms: list[str] = []

    def add_symptom(s: str) -> None:
        if s not in used and len(symptoms) < 4:
            symptoms.append(s)
            used.add(s)

    if "mono_library" in special_flags:
        add_symptom(SPECIAL_SYMPTOMS["mono_library"].format(total=total_games))

    if "backlog_cemetery" in special_flags:
        played = sum(1 for g in games if g.get("playtime_forever", 0) > 30)
        add_symptom(SPECIAL_SYMPTOMS["backlog_cemetery"].format(total=total_games, played=played))

    if "high_hours" in special_flags:
        top_game = max(games, key=lambda g: g.get("playtime_forever", 0))
        hours = _minutes_to_hours(top_game["playtime_forever"])
        days = round(hours / 24, 1)
        add_symptom(SPECIAL_SYMPTOMS["high_hours"].format(
            hours=hours, game=top_game["name"], days=days,
        ))

    if "low_hours" in special_flags:
        abandoned = [
            g for g in games
            if 0 < _minutes_to_hours(g.get("playtime_forever", 0)) < LOW_HOURS_THRESHOLD
        ]
        if abandoned:
            pick = random.choice(abandoned)
            hours = _minutes_to_hours(pick["playtime_forever"])
            add_symptom(SPECIAL_SYMPTOMS["low_hours"].format(game=pick["name"], hours=hours))

    if is_diverse and len(symptoms) < 3:
        add_symptom(SPECIAL_SYMPTOMS["diverse_library"])

    # Preenche com sintomas das categorias dominantes
    needed = 4 - len(symptoms)
    if needed > 0 and dominant_cats:
        for s in _pick_unique_symptoms(dominant_cats, exclude=used, count=needed):
            add_symptom(s)

    if not symptoms:
        symptoms = ["Biblioteca com jogos não catalogados pela ciência moderna"]

    # --- Prognóstico ---
    if "mono_library" in special_flags:
        prog = SPECIAL_PROGNOSIS["mono_library"]
    elif "backlog_cemetery" in special_flags:
        prog = SPECIAL_PROGNOSIS["backlog_cemetery"]
    elif dominant_cats and dominant_cats[0] in PROGNOSIS:
        prog = random.choice(PROGNOSIS[dominant_cats[0]])
    else:
        prog = "Prognóstico: incerto. Jogue mais e me informe."

    # --- Remédio ---
    remedy = "Prescrição: desinstale tudo e saia para caminhar. Receita universal do Dr. K."
    if dominant_cats:
        for cat in dominant_cats:
            if cat in REMEDIES and REMEDIES[cat]:
                remedy = random.choice(REMEDIES[cat])
                break

    return {
        "patient": username,
        "cid": cid,
        "symptoms": symptoms,
        "prognosis": prog,
        "remedy": remedy,
        "dominant_categories": dominant_cats,
        "special_flags": special_flags,
        "total_games": total_games,
    }

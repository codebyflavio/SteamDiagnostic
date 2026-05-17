"""
Classifica jogos Steam em categorias internas.
O índice é pré-computado uma vez na importação para evitar
iteração linear em cada chamada de categorize_games().
"""

GAME_CATEGORY_MAP: dict[str, str] = {
    # Souls-like
    "dark souls": "souls_like",
    "elden ring": "souls_like",
    "sekiro": "souls_like",
    "bloodborne": "souls_like",
    "lies of p": "souls_like",
    "hollow knight": "souls_like",
    "salt and sanctuary": "souls_like",
    "nioh": "souls_like",
    "mortal shell": "souls_like",
    "lords of the fallen": "souls_like",
    "remnant": "souls_like",
    "surge": "souls_like",
    "code vein": "souls_like",
    "wo long": "souls_like",
    "star wars jedi": "souls_like",
    "blasphemous": "souls_like",
    "nine sols": "souls_like",

    # FPS Competitivo
    "counter-strike": "fps_competitivo",
    "cs2": "fps_competitivo",
    "cs:go": "fps_competitivo",
    "rainbow six": "fps_competitivo",
    "battlefield": "fps_competitivo",
    "call of duty": "fps_competitivo",
    "team fortress": "fps_competitivo",
    "tf2": "fps_competitivo",
    "hunt: showdown": "fps_competitivo",
    "pubg": "fps_competitivo",
    "escape from tarkov": "fps_competitivo",
    "hell let loose": "fps_competitivo",
    "squad": "fps_competitivo",
    "insurgency": "fps_competitivo",
    "ready or not": "fps_competitivo",

    # Hero Shooter
    "valorant": "hero_shooter",
    "overwatch": "hero_shooter",
    "apex legends": "hero_shooter",
    "marvel rivals": "hero_shooter",
    "paladins": "hero_shooter",
    "battleborn": "hero_shooter",
    "gigantic": "hero_shooter",
    "gundam evolution": "hero_shooter",
    "deadlock": "hero_shooter",

    # ARPG
    "path of exile": "arpg",
    "diablo": "arpg",
    "grim dawn": "arpg",
    "torchlight": "arpg",
    "last epoch": "arpg",
    "wolcen": "arpg",
    "victor vran": "arpg",
    "titan quest": "arpg",
    "sacred": "arpg",
    "warhammer: inquisitor": "arpg",
    "undecember": "arpg",

    # Battle Royale
    "fortnite": "battle_royale",
    "warzone": "battle_royale",
    "the finals": "battle_royale",
    "super people": "battle_royale",
    "naraka": "battle_royale",
    "bloodhunt": "battle_royale",

    # Sandbox
    "minecraft": "sandbox",
    "terraria": "sandbox",
    "starbound": "sandbox",
    "roblox": "sandbox",
    "garry's mod": "sandbox",
    "gmod": "sandbox",
    "creativerse": "sandbox",
    "lego worlds": "sandbox",
    "vintage story": "sandbox",

    # Survival
    "rust": "survival",
    "ark": "survival",
    "the forest": "survival",
    "sons of the forest": "survival",
    "valheim": "survival",
    "subnautica": "survival",
    "don't starve": "survival",
    "green hell": "survival",
    "the long dark": "survival",
    "7 days to die": "survival",
    "raft": "survival",
    "stranded deep": "survival",
    "conan exiles": "survival",
    "icarus": "survival",
    "grounded": "survival",
    "enshrouded": "survival",
    "palworld": "survival",
    "satisfactory": "survival",
    "astroneer": "survival",

    # RPG
    "the witcher": "rpg",
    "skyrim": "rpg",
    "baldur's gate": "rpg",
    "pathfinder": "rpg",
    "divinity": "rpg",
    "dragon age": "rpg",
    "mass effect": "rpg",
    "final fantasy": "rpg",
    "cyberpunk": "rpg",
    "fallout": "rpg",
    "pillars of eternity": "rpg",
    "tyranny": "rpg",
    "torment": "rpg",
    "wasteland": "rpg",
    "disco elysium": "rpg",
    "solasta": "rpg",
    "dragon's dogma": "rpg",

    # Esporte
    "fifa": "esporte",
    "ea sports fc": "esporte",
    "pro evolution": "esporte",
    "efootball": "esporte",
    "nba 2k": "esporte",
    "nhl": "esporte",
    "madden": "esporte",
    "rocket league": "esporte",
    "football manager": "esporte",
    "motorsport": "esporte",
    "wrestling": "esporte",
    "mlb the show": "esporte",

    # Roguelike
    "hades": "roguelike",
    "dead cells": "roguelike",
    "binding of isaac": "roguelike",
    "enter the gungeon": "roguelike",
    "slay the spire": "roguelike",
    "noita": "roguelike",
    "risk of rain": "roguelike",
    "gunfire reborn": "roguelike",
    "vampire survivors": "roguelike",
    "deep rock galactic": "roguelike",
    "returnal": "roguelike",
    "spelunky": "roguelike",
    "crypt of the necrodancer": "roguelike",
    "monster train": "roguelike",
    "across the obelisk": "roguelike",
    "roboquest": "roguelike",
    "cult of the lamb": "roguelike",

    # Simulador
    "stardew valley": "simulador",
    "farming simulator": "simulador",
    "cities skylines": "simulador",
    "cities: skylines": "simulador",
    "planet coaster": "simulador",
    "two point": "simulador",
    "powerwash simulator": "simulador",
    "house flipper": "simulador",
    "car mechanic simulator": "simulador",
    "euro truck": "simulador",
    "american truck": "simulador",
    "the sims": "simulador",
    "rimworld": "simulador",
    "dwarf fortress": "simulador",
    "prison architect": "simulador",
    "manor lords": "simulador",
    "frostpunk": "simulador",
    "oxygen not included": "simulador",
    "medieval dynasty": "simulador",

    # Visual Novel
    "doki doki": "visual_novel",
    "ace attorney": "visual_novel",
    "danganronpa": "visual_novel",
    "steins;gate": "visual_novel",
    "clannad": "visual_novel",
    "fate/": "visual_novel",
    "higurashi": "visual_novel",
    "va-11 hall-a": "visual_novel",
    "coffee talk": "visual_novel",

    # Estratégia
    "civilization": "estrategia",
    "total war": "estrategia",
    "age of empires": "estrategia",
    "starcraft": "estrategia",
    "company of heroes": "estrategia",
    "crusader kings": "estrategia",
    "europa universalis": "estrategia",
    "hearts of iron": "estrategia",
    "stellaris": "estrategia",
    "xcom": "estrategia",
    "humankind": "estrategia",
    "endless legend": "estrategia",
    "sins of a solar empire": "estrategia",
    "homeworld": "estrategia",
    "warcraft iii": "estrategia",
    "age of mythology": "estrategia",

    # Horror
    "resident evil": "horror",
    "silent hill": "horror",
    "outlast": "horror",
    "amnesia": "horror",
    "phasmophobia": "horror",
    "dead by daylight": "horror",
    "little nightmares": "horror",
    "visage": "horror",
    "soma": "horror",
    "layers of fear": "horror",
    "alan wake": "horror",
    "alien isolation": "horror",
    "five nights": "horror",
    "fnaf": "horror",
    "the quarry": "horror",
    "until dawn": "horror",
    "madison": "horror",

    # Plataforma
    "celeste": "plataforma",
    "ori and the": "plataforma",
    "cuphead": "plataforma",
    "shovel knight": "plataforma",
    "super meat boy": "plataforma",
    "rayman": "plataforma",
    "a hat in time": "plataforma",
    "axiom verge": "plataforma",
    "metroid": "plataforma",
    "pizza tower": "plataforma",
    "neon white": "plataforma",

    # MMO
    "world of warcraft": "mmo",
    "final fantasy xiv": "mmo",
    "ffxiv": "mmo",
    "guild wars": "mmo",
    "elder scrolls online": "mmo",
    "black desert": "mmo",
    "new world": "mmo",
    "lost ark": "mmo",
    "runescape": "mmo",
    "star wars: the old republic": "mmo",
    "albion online": "mmo",
}

# Pré-computa lista ordenada por tamanho de keyword (keywords mais longas têm prioridade)
# Isso garante que "final fantasy xiv" seja testado antes de "final fantasy"
_SORTED_KEYWORDS: list[tuple[str, str]] = sorted(
    GAME_CATEGORY_MAP.items(),
    key=lambda x: -len(x[0]),
)


def categorize_games(games: list[dict]) -> dict[str, list[dict]]:
    result: dict[str, list[dict]] = {}
    for game in games:
        name = game.get("name", "").lower().strip()
        matched = False
        for keyword, category in _SORTED_KEYWORDS:
            if keyword in name:
                result.setdefault(category, []).append(game)
                matched = True
                break
        if not matched:
            result.setdefault("outros", []).append(game)
    return result


def get_dominant_categories(categorized: dict[str, list[dict]], top_n: int = 3) -> list[str]:
    filtered = {k: v for k, v in categorized.items() if k != "outros"}
    sorted_cats = sorted(filtered.items(), key=lambda x: len(x[1]), reverse=True)
    return [cat for cat, _ in sorted_cats[:top_n]]

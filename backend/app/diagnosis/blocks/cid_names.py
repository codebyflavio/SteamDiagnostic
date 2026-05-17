"""
Nomes falsos de transtornos psicológicos por categoria.
"""

CID_NAMES: dict[str, list[str]] = {
    "souls_like": [
        "TDM-S — Transtorno de Dor Masoquista Seletiva (Crônica)",
        "TPIV — Transtorno de Prazer Invertido por Violência Pixelada",
        "SDR-III — Síndrome do Desafio Ridículo Grau III",
        "TAH — Transtorno de Aceitação de Humilhação Voluntária",
        "FICD — Fixação Intransigente em Conteúdo Difícil",
        "SESG — Síndrome de Estocolmo com Sistema de Jogo",
        "TNE — Transtorno de Negação do Entretenimento Acessível",
    ],
    "fps_competitivo": [
        "THCS — Transtorno de Hardstuck Crônico Severo (Recorrente)",
        "DPI-FPS — Delírio de Perseguição Individual em Ambiente Multijogador",
        "SRCT — Síndrome da Responsabilidade Coletiva Terceirizada",
        "TDAH-Gamer — Transtorno do Déficit de Aim com Hiperatividade no Chat",
        "SPTE — Síndrome de Projeção Total por Eliminação",
        "DCC — Distúrbio de Calibração Crônica de Periféricos",
        "TRAC — Transtorno de Rank Aspiracional Crônico",
    ],
    "hero_shooter": [
        "DOCH — Distúrbio Obsessivo-Compulsivo com Herói Principal",
        "SMFN — Síndrome do Meta-Follower Nervoso",
        "TPRS — Transtorno de Percepção de Roster como Status Social",
        "RENI — Reação Emocional a Nerf Indevido",
        "FIHS — Fixação de Identidade em Hero Shooter",
    ],
    "arpg": [
        "TOB-C — Transtorno Obsessivo de Build Compulsivo",
        "DSL — Distúrbio de Síndrome de Liga (Recorrente Sazonal)",
        "TPGI — Transtorno de Perfeição de Gear Infinita",
        "SDIB — Síndrome da Dependência de Item Bis",
        "FIAP — Fixação em Ineficiência por Análise Paralítica",
        "TOCC — Transtorno Obsessivo-Compulsivo de Crafting",
    ],
    "battle_royale": [
        "TCIP — Transtorno de Círculo como Inimigo Pessoal",
        "SAT2 — Síndrome do Algoritmo de Targeting Persecutório",
        "DPCM — Delírio de Perseguição por Círculo Mágico",
        "FOBS — Fixação Obsessiva em Batalha Solo",
    ],
    "sandbox": [
        "TCP — Transtorno Compulsivo de Planejamento (Sem Execução)",
        "SPI — Síndrome do Projeto Inacabado Infinito",
        "DFNC — Disfunção de Finalização Narrativa Crônica",
        "TEI — Transtorno de Expansão Ilimitada sem Propósito",
        "TOAD — Transtorno Obsessivo de Ambientação e Design",
        "SPRI — Síndrome do Perfeccionista Que Recomeça Infinitamente",
    ],
    "survival": [
        "SAE — Síndrome da Ansiedade de Extinção de Barra Virtual",
        "TOC-S — TOC de Sobrevivência em Ambiente Controlado",
        "TSR — Transtorno de Stockpile Resistente ao Tratamento",
        "TPAN — Transtorno de Paranoia por Ambiente Aparentemente Não-Hostil",
        "SPBA — Síndrome de Perda de Base por Ausência",
    ],
    "rpg": [
        "TICE — Transtorno de Incapacidade de Comprometimento Existencial",
        "SPI-R — Síndrome de Paralisia por Imersão em Roleplay",
        "DPA — Distúrbio de Procrastinação por Alternativas Narrativas",
        "THSM — Transtorno de Heroísmo de Segunda Mão",
        "DSNP — Distúrbio de Sabedoria de NPC Preferencial",
        "TCRP — Transtorno Compulsivo de Reinício por Perfeccionismo",
        "SDLC — Síndrome de Dependência de Lore de Contexto",
    ],
    "esporte": [
        "DCVR — Delírio de Competência Via Representação Digital",
        "SEFV — Síndrome do Especialista FIFA Voluntário Não-Solicitado",
        "TPVC — Transtorno de Projeção de Vitória Virtual em Campo Real",
        "CMEA — Complexo de Mourinho em Ambiente Artificial Controlado",
        "DFUR — Distúrbio de Fidelidade a Ultimate Team Recorrente",
        "TERF — Transtorno de Expertise em Rating de FIFA",
    ],
    "roguelike": [
        "TVMD — Transtorno de Vício em Morte e Derrota Repetida",
        "SDCI — Síndrome da Dependência de Caos Imprevisível",
        "SPRC — Síndrome de Procrastinação via Run Compulsiva",
        "TNI-R — Transtorno de Negação da Incompetência Roguelike",
        "FPIP — Fixação em Próxima Item Pool",
        "DSMR — Distúrbio de Sono por Mais Uma Run",
    ],
    "simulador": [
        "DRV — Dissociação de Realidade Via Virtude Virtual",
        "TSVR — Transtorno de Substituição de Vida Real por Simulação",
        "SFV — Síndrome da Fazenda Virtual Prioritária",
        "TGEP — Transtorno de Gestão Produtiva Escapista",
        "DERD — Distúrbio de Eficiência Real Deslocada",
        "SPMV — Síndrome de Produtividade Mal-Direcionada Virtual",
    ],
    "visual_novel": [
        "TFPE — Transtorno de Fixação em Personagem Pixelado Bidimensional",
        "DEN — Distúrbio de Empatia Narrativa Desproporcional",
        "SPNR — Síndrome do Protagonismo Narrativo Reativo",
        "TRPE — Transtorno de Relacionamento com Personagem Estático",
        "SRVN — Síndrome de Rota Visual Não-Terminada",
        "DPMS — Distúrbio de Paralisia por Medo de Spoiler Próprio",
    ],
    "estrategia": [
        "TOHP — Transtorno Obsessivo de Hiperplanejamento Estratégico",
        "SGA — Síndrome do General de Armchair Determinado",
        "DAMA — Distúrbio de Análise em Detrimento de Ação",
        "TPPM — Transtorno de Paralisia Por Micromanagement",
        "OMTS — One More Turn Syndrome (Clássico Não-Tratável)",
        "SCDP — Síndrome da Colonização Digital como Procrastinação",
    ],
    "horror": [
        "TAMS — Transtorno de Atração por Medo em Ambiente Seguro",
        "SMED — Síndrome do Medo com Endorfina Diferida",
        "DAM-I — Distúrbio de Auto-Mutilação Emocional Interativa",
        "THCM — Transtorno de Horror Crônico com Máscara de Coragem",
        "SRPC — Síndrome da Resistência Performática ao Conteúdo",
        "DEPV — Desconforto Emocional Periódico Voluntário",
    ],
    "plataforma": [
        "TRPI — Transtorno de Repetição de Plataforma Infinita",
        "SPC — Síndrome do Perfeccionismo de Coleta Compulsiva",
        "DPCI — Distúrbio de Persistência por Condicionamento Iterativo",
        "TPCZ — Transtorno de Porcentagem de Conclusão como Zen",
        "SCOS — Síndrome de Completude Obsessiva de Segredo",
    ],
    "mmo": [
        "TDMV — Transtorno de Dependência de Mundo Virtual",
        "SRGD — Síndrome do Raid como Gestão de Dependências",
        "TPGE — Transtorno de Progressão de Gear como Existência",
        "DEMS — Distúrbio de Endgame como Sentido de Vida",
        "SPGD — Síndrome do Patch de Balanço como Drama Existencial",
    ],
}

HYBRID_SUFFIXES: dict[str, str] = {
    "souls_like": "Masoquista",
    "fps_competitivo": "Hardstuck",
    "hero_shooter": "Meta-Dependente",
    "arpg": "Build-Compulsivo",
    "battle_royale": "Círculo-Fóbico",
    "sandbox": "Construtor-Eterno",
    "survival": "Sobrevivencialista",
    "rpg": "Roleplay-Preso",
    "esporte": "FIFA-Dependente",
    "roguelike": "Run-Compulsivo",
    "simulador": "Simulacionista",
    "visual_novel": "2D-Apegado",
    "estrategia": "Hiperanalítico",
    "horror": "Autoflagelante",
    "plataforma": "Perfeccionista",
    "mmo": "Raid-Obcecado",
}


# Merge new generated content
from ._new_content import NEW_CID_NAMES as _NEW_CID
for _cat, _names in _NEW_CID.items():
    CID_NAMES.setdefault(_cat, []).extend(_names)

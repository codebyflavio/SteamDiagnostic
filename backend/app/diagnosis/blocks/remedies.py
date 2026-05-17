"""
Remédios irônicos por categoria.
"""

REMEDIES: dict[str, list[str]] = {
    "souls_like": [
        "Receita: 30 dias de Stardew Valley no modo pacífico, sem combate, só plantando cenouras. Tome com água.",
        "Prescrição: instale qualquer jogo com modo fácil e jogue sem culpa. Terapia de exposição gradual à vitória.",
        "Receita: Unpacking. Nenhum inimigo, nenhuma morte, apenas organizar objetos. O choque pode ser fatal, mas é necessário.",
        "Prescrição: Firewatch. 4h, trilha sonora linda, zero possibilidade de morrer. O sistema nervoso central agradece.",
        "Receita: Powerwash Simulator. Lavar coisas. Nenhuma ameaça existencial. Nenhum boss. Apenas água e sujeira.",
    ],
    "fps_competitivo": [
        "Prescrição: 2 semanas de Journey, sem inimigos, sem chat, sem ranking. Silêncio total obrigatório.",
        "Receita: Animal Crossing por 30 dias. Sem competição, sem tilt, apenas vilajejos e pescaria às 7h da manhã.",
        "Prescrição: desativar o chat de voz permanentemente em todos os jogos. Manter por 6 meses.",
        "Receita: Stardew Valley. Seus 'inimigos' são corvos comendo as suas culturas. Proporcionalmente manejável.",
        "Prescrição: Inside ou Limbo — sem competição, sem rank, sem teammates para culpar. Apenas existir.",
    ],
    "hero_shooter": [
        "Receita: qualquer jogo single-player sem multiplayer online. Descubra que a culpa era sua o tempo todo.",
        "Prescrição: Celeste. Um personagem, uma jornada, zero meta para seguir. Terapia de identidade fixa.",
        "Receita: um jogo de estratégia por turnos. Aprenda a pensar antes de agir. Conceito revolucionário.",
        "Prescrição: Detroit: Become Human. Suas escolhas têm consequências reais na narrativa. Treinamento de responsabilidade.",
    ],
    "arpg": [
        "Receita: qualquer jogo com narrativa linear de 20h. Experimente o conceito radical de 'terminar algo'.",
        "Prescrição: The Last of Us. Uma build, uma história, um fim. Não há próxima temporada. Respire.",
        "Receita: Hades. Sim, tem progressão. Mas tem uma história que termina. Transição gradual.",
        "Prescrição: sair da planilha de builds e jogar qualquer coisa por prazer puro, sem otimização. 30 minutos. Só isso.",
    ],
    "battle_royale": [
        "Receita: qualquer jogo cooperativo onde a vitória é coletiva. Aprenda que outros humanos podem ser aliados.",
        "Prescrição: Minecraft no modo criativo. Sem círculo, sem eliminação, sem top 1. Apenas construir.",
        "Receita: It Takes Two. Precisa de outro jogador. Precisa cooperar. O oposto de tudo que você faz.",
    ],
    "sandbox": [
        "Receita: qualquer jogo linear com 4h de duração. Termine algo pelo amor de qualquer divindade.",
        "Prescrição: Inside ou Limbo — sem inventário, sem base, apenas ir para frente. Choque terapêutico controlado.",
        "Receita: Portal 1. Curto, objetivo, sem possibilidade de construir nada. Cura documentada em 3h.",
        "Prescrição: Firewatch. Um personagem, uma floresta, um fim. Sem blocos. Sem crafting. Apenas caminhar.",
    ],
    "survival": [
        "Prescrição: Stardew Valley modo relaxado. Sem chance de morrer, com vizinhos amigáveis. Impacto terapêutico imediato.",
        "Receita: qualquer visual novel. Literalmente nada vai te matar. Nada. Relaxe. Respire.",
        "Prescrição: Unpacking. A maior ameaça é decidir onde colocar o abajur. Sem barra de fome.",
        "Receita: A Short Hike. Duração: 2h. Nível de perigo: zero. Existe apenas pra ser bonito.",
    ],
    "rpg": [
        "Receita: Superhot — sem criação de personagem, sem diálogo, apenas reflexo. 2h e acabou. Decisão tomada.",
        "Prescrição: terminar qualquer jogo da biblioteca atual antes de iniciar outro. Um de cada vez.",
        "Receita: Celeste. História linear, sem ramificações, sem escolhas de diálogo. Terapia cognitiva de comprometimento.",
        "Prescrição: qualquer metroidvania. Há um caminho. Ele está lá. Você não precisa decidir o que seu personagem sente sobre isso.",
    ],
    "esporte": [
        "Prescrição: sair de casa e assistir um jogo real. O gramado existe fora do monitor.",
        "Receita: Rocket League. Ao menos o gameplay é mecânico puro e não financeiramente predatório.",
        "Prescrição: pausar o Ultimate Team por 30 dias. Calcular o total gasto. Imediatamente não calcular.",
        "Receita: Football Manager. Ainda é futebol virtual, mas pelo menos tem dados reais e não pacotes de FUT.",
    ],
    "roguelike": [
        "Receita: qualquer jogo com narrativa linear que termina. Experimente o conceito alienígena chamado 'fim'.",
        "Prescrição: The Last of Us. Uma run. Com começo, meio e fim. A revolucionária estrutura narrativa completa.",
        "Receita: Firewatch. 4h, história, sem morte possível. O sistema nervoso agradece em 2h.",
        "Prescrição: Disco Elysium. Tem RNG, mas tem fim. Transição suave para o mundo com bordas.",
    ],
    "simulador": [
        "Prescrição: sair para realizar a tarefa evitada há 3 semanas. O jogo continuará aqui depois.",
        "Receita: qualquer jogo de ação sem pausa, tipo Doom. Menos gestão, mais adrenalina não-administrada.",
        "Prescrição: Vampire Survivors. Gestão mínima, caos máximo. Transição gradual para o impulsivo.",
        "Receita: Celeste. Sem orçamento, sem gestão. Apenas subir uma montanha. Uma tarefa. Uma pessoa.",
    ],
    "visual_novel": [
        "Receita: um livro físico. De papel. Com palavras. Sem sprites, sem trilha sonora lo-fi, sem escolhas.",
        "Prescrição: jogar qualquer coisa que exija reflexo. Mostre que o mundo pode reagir a você em tempo real.",
        "Receita: Hades. Tem história rica, tem personagens carismáticos. E eles tentam te matar. Equilíbrio saudável.",
        "Prescrição: Disco Elysium. Ainda é narrativo, mas você tem um corpo que pode falhar. Contato com consequência.",
    ],
    "estrategia": [
        "Prescrição: Doom Eternal. Não há tempo para planejar. Apenas atirar. Terapia de ação imediata.",
        "Receita: qualquer roguelike sem pausa ativa. Decisões em 0.3 segundos. Treinamento de impulsividade funcional.",
        "Prescrição: Among Us. Estratégia social, sem planilhas. Inclui contato humano como efeito colateral.",
        "Receita: Vampire Survivors. Decisões simples, inimigos óbvios, vitória automática com o tempo. Sem geopolítica.",
    ],
    "horror": [
        "Receita: Stardew Valley. A coisa mais assustadora é perder uma colheita para o corvo.",
        "Prescrição: Mario Kart. Cores brilhantes, música animada, zero criatura perseguindo você nos corredores.",
        "Receita: Powerwash Simulator. Lavar coisas. Nenhuma ameaça existencial. Terapia aquática comprovada.",
        "Prescrição: A Short Hike. Pássaros, montanhas, céu azul. O oposto de qualquer coisa que você joga.",
    ],
    "plataforma": [
        "Receita: qualquer RPG de ritmo lento onde você pode ficar parado admirando a paisagem.",
        "Prescrição: The Sims. Zero plataformas, zero saltos, apenas drama doméstico administrável.",
        "Receita: Minecraft modo criativo. Sem objetivo, sem coleta obrigatória, sem porcentagem de conclusão.",
        "Prescrição: Journey. Sem checkpoints desnecessários, sem coleta, apenas um caminho e o destino.",
    ],
    "mmo": [
        "Prescrição: qualquer jogo single-player de 20h. Sem guild, sem raid, sem compromisso online.",
        "Receita: Stardew Valley. Os 'outros jogadores' são NPCs que nunca te decepcionam ou saem da guild.",
        "Prescrição: Outer Wilds. Exploração solo, sem progressão de gear, apenas descoberta. Terapia de desapego.",
        "Receita: Red Dead Redemption 2. Um personagem, uma história, sem subscription fee.",
    ],
}

"""
Prognósticos fictícios por categoria.
"""

PROGNOSIS: dict[str, list[str]] = {
    "souls_like": [
        "O paciente continuará morrendo nos mesmos bosses pelos próximos 6 meses e chamará isso de 'progresso'. Prognóstico: irreversível.",
        "Com tratamento adequado (desinstalar o jogo), pode recuperar 40% da sanidade. Sem tratamento: continuará citando FromSoftware em conversas de happy hour.",
        "Evoluirá naturalmente para 'vou ensinar meu filho de 3 anos a jogar Dark Souls'. A sociedade não pode fazer nada.",
        "Prognóstico a longo prazo: colecionará todos os jogos do gênero, terminará metade, sofrendo em todos eles. Com orgulho.",
        "O paciente nunca vai admitir que o jogo é difícil demais. Seguirá jogando por pura teimosia existencial.",
    ],
    "fps_competitivo": [
        "Permanecerá hardstuck até o fim dos tempos, comprará um mouse novo a cada temporada e acreditará que isso vai mudar algo.",
        "Prognóstico sombrio: o rank não vai subir. A pressão arterial sim. Os dois no mesmo ritmo.",
        "Em 5 anos, estará em lobbies de rank baixo 'esnobando' iniciantes com a autoridade de quem nunca subiu de Silver.",
        "Continuará instalando e desinstalando o jogo em ciclos de 72 horas, como as estações do ano.",
        "A qualidade do sono está diretamente correlacionada com o resultado das últimas 3 partidas. O médico real está preocupado.",
    ],
    "hero_shooter": [
        "O personagem favorito receberá um nerf no próximo patch. O paciente reagirá como se fosse um luto.",
        "Continuará trocando de main a cada temporada enquanto afirma ser 'flexível e adaptável ao meta'.",
        "Em 6 meses desenvolverá opiniões extremamente específicas sobre ticks de servidor que ninguém ao redor vai entender.",
        "Prognóstico: a skin nova vai resolver o desempenho ruim. Não vai. Mas vai ser comprada assim mesmo.",
    ],
    "arpg": [
        "A build 'definitiva' nunca será encontrada. A jornada é o ponto. O paciente não aceitará isso.",
        "Cada nova temporada é uma nova chance de recomeçar e cometer os mesmos erros com entusiasmo renovado.",
        "Prognóstico: a próxima liga vai ser diferente. Não vai. Mas as próximas 500h provarão isso empiricamente.",
        "O paciente saberá tudo sobre o endgame teórico e praticará com competência questionável por 800 horas.",
    ],
    "battle_royale": [
        "Continuará chegando no top 5 e perdendo para alguém que 'claramente estava hacking'.",
        "A vitória definitiva está sempre a uma partida de distância. Essa distância nunca diminui.",
        "Prognóstico: as skins novas não vão melhorar o aim. O paciente ainda assim irá comprá-las como experimento.",
    ],
    "sandbox": [
        "Jamais terminará qualquer projeto. Os saves acumularão como arquivos que 'vão organizar depois'.",
        "Em 10 anos, terá 47 mundos incompletos e nenhuma história para contar. Cada um com um nome especial.",
        "O terapeuta real desistiu. O jogo continua esperando pacientemente com a mesma indiferença de sempre.",
        "Prognóstico: a base nova vai ser diferente das outras 23. Não vai. Mas o processo de construção é a cura.",
    ],
    "survival": [
        "Desenvolverá ansiedade funcional em ambientes físicos sem barra de stamina visível.",
        "Continuará acordando às 3h preocupado com servidores que deletaram a base há 2 semanas.",
        "Com o tempo, aprenderá a sobreviver no jogo. Na vida real, o prognóstico continua em aberto.",
        "Em algum momento começará a fazer planilhas de recursos reais com a mesma lógica do inventário virtual.",
    ],
    "rpg": [
        "Nunca terminará a história principal, mas saberá tudo sobre lore de NPCs que aparecem por 40 segundos.",
        "Continuará criando personagens novos a cada 3 sessões sem chegar ao primeiro boss.",
        "Prognóstico: morrerá com 12 saves no tutorial e uma biblioteca de builds não testadas.",
        "Já pesquisou 'qual classe é mais forte' antes de decidir como quer jogar. Isso não vai mudar.",
        "A decisão de diálogo 'errada' de 3 horas atrás ainda incomoda. Sempre vai incomodar.",
    ],
    "esporte": [
        "Continuará achando que Ultimate Team é um investimento financeiro com retorno emocional positivo.",
        "Em breve dará palpites táticos sobre o clube favorito com base em experiência exclusivamente virtual.",
        "Prognóstico financeiro: negativo. Prognóstico tático real: sem correlação comprovada com o jogo.",
        "Já discutiu com alguém sobre um jogador real usando argumentos baseados no rating do FIFA. Repetirá.",
    ],
    "roguelike": [
        "Vai continuar dizendo 'só mais uma run' até o sol completar seu ciclo de vida estelar.",
        "Nunca saberá quando parar. O jogo foi projetado exatamente para isso. Parabéns ao desenvolvedor.",
        "Prognóstico: excelente para a receita da desenvolvedora. Para a saúde do paciente: inconclusivo.",
        "A run perfeita teórica existe. O paciente não vai dormir direito até executá-la. Pode demorar anos.",
        "Cada morte é 'quase lá'. Matematicamente impossível, mas psicologicamente necessário acreditar nisso.",
    ],
    "simulador": [
        "Desenvolverá mais habilidades gerenciais virtuais do que qualquer curso de gestão — inaplicáveis no mundo real.",
        "A fazenda/cidade virtual prosperará. O quarto continuará no mesmo estado entrópico de sempre.",
        "Em 2 anos será o melhor prefeito digital da região sudeste. O curriculum real não vai mudar.",
        "Prognóstico: o jogo criou um senso de produtividade que a vida real ainda não aprendeu a replicar.",
    ],
    "visual_novel": [
        "Continuará recomendando o jogo para amigos sem perceber que está pedindo companhia nessa jornada emocional.",
        "Vai escolher a rota ruim de propósito para 'ter a experiência completa'. Isso é auto-sabotagem documentada.",
        "Prognóstico emocional: instável. Prognóstico de choro por sprite 2D: garantido.",
        "Já buscou o guia antes de fazer qualquer escolha difícil. Aplicará essa lógica na vida real em breve.",
    ],
    "estrategia": [
        "Continuará perdendo para a IA no nível Médio enquanto planeja estratégias de dominação continental.",
        "Em algum momento aplicará o conceito de 'expansão cautelosa' em uma conversa de trabalho. Será demitido.",
        "Prognóstico: excelente general virtual. Rendimento no mundo sem pausa e sem desfazer: questionável.",
        "O 'one more turn' às 2h da manhã é inevitável. Sempre foi. Sempre será.",
    ],
    "horror": [
        "Continuará comprando jogos de terror, jogando 15 minutos e afirmando com convicção que 'não era tão assustador'.",
        "O reflexo de susto estará condicionado para qualquer porta que abra devagar por tempo indeterminado.",
        "Prognóstico: a coleção de horror crescerá inversamente proporcional ao tempo efetivamente jogado.",
        "Assistirá o restante do jogo no YouTube. Dirá que 'tanto faz, o importante é a história'.",
    ],
    "plataforma": [
        "Vai dedicar 6 horas a um item opcional que não altera nada na jogabilidade ou narrativa.",
        "O 100% de conclusão está a exatamente 47 tentativas de distância. O paciente não vai parar antes.",
        "Prognóstico: dedos eventualmente doloridos, satisfação questionável, nenhum item não coletado.",
        "Conhecerá cada milímetro do mapa antes de avançar. O jogo tem 40 horas. Levará 120.",
    ],
    "mmo": [
        "O personagem virtual tem mais histórias investidas do que qualquer amizade da vida real.",
        "Continuará pagando a assinatura mesmo em meses que jogar menos de 10 minutos 'só para manter o acesso'.",
        "Prognóstico: o endgame é inalcançável por design. O paciente continuará perseguindo-o assim mesmo.",
        "A guild vai implodir. Sempre implode. O paciente vai entrar em outra e repetir o ciclo.",
    ],
}

SPECIAL_PROGNOSIS = {
    "mono_library": "Pagou por uma biblioteca inteira mas usa como assinatura de um único jogo. O algoritmo da Steam desistiu de recomendar qualquer coisa nova há meses.",
    "backlog_cemetery": "O cemitério de backlog crescerá a cada promoção. O paciente comprará tudo na próxima sale e jogará 0.5h de cada um. Ciclo sem tratamento conhecido.",
    "diverse_library": "A terapia não funcionou porque o paciente não consegue decidir qual transtorno tem. Cada sessão revela uma identidade gamer completamente nova.",
}


# Merge new generated content
from ._new_content import NEW_PROGNOSIS as _NEW_PRG
for _cat, _prgs in _NEW_PRG.items():
    PROGNOSIS.setdefault(_cat, []).extend(_prgs)

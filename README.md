# 🧠 Dr. K. — Psicólogo Gamer™

> Diagnósticos psicológicos **100% fictícios** baseados na sua biblioteca Steam.  
> Completamente desnecessário. Absolutamente obrigatório.

---

## Stack

| Camada | Tecnologia |
|--------|-----------|
| Frontend | Next.js 15 (App Router) + Tailwind CSS |
| Backend | FastAPI (Python) |
| Dados | Steam Web API |
| Deploy Frontend | Vercel |
| Deploy Backend | Render |

---

## Como funciona

1. Usuário insere o ID ou URL do perfil Steam
2. Backend busca o perfil e a lista de jogos via Steam Web API
3. Motor de diagnóstico categoriza os jogos em 16 gêneros e gera um laudo fictício
4. Resultado é codificado em base64url e compartilhável via link direto (sem banco de dados)

---

## Rodando localmente

### Backend

```bash
cd backend
python -m venv .venv
source .venv/bin/activate  # Windows: .venv\Scripts\activate
pip install -r requirements.txt
cp .env.example .env       # adicione sua STEAM_API_KEY
python -m uvicorn app.main:app --reload
```

> API disponível em `http://localhost:8000`  
> Documentação em `http://localhost:8000/docs`

### Frontend

```bash
cd frontend
npm install
cp .env.example .env.local  # configure NEXT_PUBLIC_API_URL=http://localhost:8000
npm run dev
```

> App disponível em `http://localhost:3000`

---

## Variáveis de ambiente

### Backend (`backend/.env`)
```env
STEAM_API_KEY=sua_chave_aqui
```

> Obtenha sua chave em: https://steamcommunity.com/dev/apikey

### Frontend (`frontend/.env.local`)
```env
NEXT_PUBLIC_API_URL=http://localhost:8000
```

---

## Categorias de diagnóstico

`Souls-like` `FPS Competitivo` `Hero Shooter` `ARPG` `Battle Royale` `Sandbox` `Survival` `RPG` `Esporte` `Roguelike` `Simulador` `Visual Novel` `Estratégia` `Horror` `Plataforma` `MMO`

---

## Aviso legal

O Dr. K. não possui CRM, formação médica ou qualquer credencial reconhecida.  
Este projeto é **100% ficção** e foi criado para fins de entretenimento.

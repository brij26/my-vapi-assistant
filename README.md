# AI Persona Assistant — Brij Patel

> A voice-enabled, RAG-powered AI persona built for the **Scaler AI Engineer Screening Assignment** — call it, chat with it, and book an interview, all without any human in the loop.

🌐 **Live Demo:** [my-vapi-assistant.vercel.app](https://my-vapi-assistant.vercel.app/)

---

## Try It Now

### 🎙️ Option 1 — Talk to the Voice Agent (Free, No Phone Needed)

Visit the live site and use the **built-in browser voice interface** to talk to **Brij Patel AI Assistant** directly — no phone call required, no cost to you.

👉 [my-vapi-assistant.vercel.app](https://my-vapi-assistant.vercel.app/)

---

### 📞 Option 2 — Call the Voice Agent

You can also call the agent directly on its phone number:

**`+1 (312) 766-8044`**

> ⚠️ **International call note:** This is a US number provisioned on the free tier. If you're calling from outside the US (e.g. India), standard international calling rates from your carrier will apply. **To avoid any cost, use the browser voice interface on the live website instead** — it's the same agent.

---

### 💬 Option 3 — Chat Interface

The live site also includes a full **chat interface** where you can:

- Ask about Brij's background, skills, and fit for the role
- Query any public GitHub repo (tech stack, design tradeoffs, commit history)
- Check availability and **book a call directly from chat**
- Test with adversarial or edge-case questions — the agent stays grounded

---

## Assignment Context

This project was built as a submission for the **Scaler AI Engineer Screening Assignment**, which required:

| Part | Requirement | Weight |
|---|---|---|
| A | Live voice agent — RAG-grounded, handles interruptions, books real calendar slots | 35% |
| B | Public chat interface — resume + GitHub Q&A, booking, adversarial-proof | 35% |
| C | Evals report — latency, hallucination rate, retrieval quality, failure modes | 30% |

Hard requirements included: voice latency < 2s, real calendar booking (Calendly / Cal.com), RAG over actual resume and GitHub repos (no hardcoded answers), and keeping the system live for 7 days post-submission.

---

## What It Does

AI Persona Assistant is a full-stack AI persona that answers questions about Brij Patel's professional background and projects. It combines retrieval-augmented generation (RAG) with a tool-enabled LangChain agent to deliver accurate, context-grounded answers — backed by a real resume and live GitHub repositories.

Key capabilities:

- **Voice interaction** — browser-based voice (free) and PSTN phone number
- **Resume Q&A** — answers grounded in PDF resume content
- **GitHub project knowledge** — fetches READMEs, commit history, and repo metadata in real time
- **RAG pipeline** — Pinecone vector search retrieves relevant context before every response
- **Calendar booking** — checks real availability and confirms meetings without human intervention
- **Hallucination prevention** — agent stays factual; says "I don't know" rather than inventing

---

## Tech Stack

| Layer | Technology |
|---|---|
| Frontend | HTML, CSS, JavaScript |
| Backend | Python, FastAPI |
| Voice (browser) | Vapi Web SDK |
| Agent / RAG | LangChain, LangChain Classic Agents |
| Vector DB | Pinecone |
| LLM | OpenAI Chat API |
| Deployment | Vercel (frontend) + Render (backend) |

---

## Architecture

```
User (Browser or Phone)
    │
    ├── Browser Voice ──► Vapi Web SDK ──► Voice Agent
    │
    ├── Phone Call ──────► +1 (312) 766-8044 (Vapi PSTN)
    │
    └── Chat UI ─────────► HTTP POST /chat
                                │
                         FastAPI Backend (main.py)
                                │
                    ┌───────────┴───────────┐
                    │                       │
           LangChain Agent (agent.py)       │
                    │                       │
           ┌────────┴────────┐              │
           │                 │              │
    GitHub Tool         RAG Retriever       │
    (github_tool.py)    (rag.py)            │
    READMEs, commits    Pinecone search     │
                                            │
                         OpenAI Chat API ◄──┘
                         (answer generation)
```

---

## Project Structure

```
├── backend/
│   ├── main.py           # FastAPI app and /chat endpoint
│   ├── agent.py          # LangChain agent with tool definitions
│   ├── github_tool.py    # GitHub helper (READMEs, commits, repo metadata)
│   ├── rag.py            # Pinecone retriever setup
│   ├── ingest.py         # Document ingestion and embedding upload
│   ├── requirements.txt  # Python dependencies
│   └── data/             # Source documents for RAG grounding
│
├── frontend/
│   ├── index.html        # Chat and voice UI
│   ├── script.js         # Frontend logic and initialization
│   ├── style.css         # Styles
│   └── components/       # Voice and chat components
│
└── data/
    └── ...               # Resume PDF and other grounding documents
```

---

## Getting Started (Self-Hosting)

### Prerequisites

- Python 3.9+
- Accounts for: OpenAI, Pinecone, GitHub, Vapi

### 1. Clone the repository

```bash
git clone https://github.com/brij26/my-vapi-assistant.git
cd my-vapi-assistant
```

### 2. Set up environment variables

Create a `.env` file in the project root:

```env
OPENAI_API_KEY=your_openai_api_key
GITHUB_TOKEN=your_github_personal_access_token
GITHUB_USERNAME=your_github_username
PINECONE_API_KEY=your_pinecone_api_key
PINECONE_ENVIRONMENT=your_pinecone_environment
PINECONE_INDEX=your_pinecone_index_name
```

### 3. Install backend dependencies

```bash
cd /workspaces/my-vapi-assistant
python3 -m pip install -r backend/requirements.txt
```

### 4. Ingest documents into Pinecone

Place your resume PDF in `backend/data/`, then run:

```bash
cd backend
python ingest.py
```

This loads PDFs, splits them into chunks, generates OpenAI embeddings, and uploads them to Pinecone.

### 5. Start the backend

```bash
uvicorn backend.main:app --reload --host 0.0.0.0 --port 8000
```

### 6. Open the frontend

Open `frontend/index.html` in your browser, or deploy to Vercel.

---

## How the RAG Pipeline Works

1. **Ingestion** — `ingest.py` loads PDFs from `backend/data/`, splits them into text chunks, and stores embeddings in Pinecone.
2. **Retrieval** — on each query, `rag.py` performs a similarity search in Pinecone to fetch the most relevant chunks.
3. **Tool use** — `github_tool.py` fetches live repo data (README, commits, metadata) from GitHub on demand.
4. **Generation** — the LangChain agent combines retrieved context with the query and calls OpenAI to produce a grounded response.

---

## Example Questions to Try

```
"Why are you the right person for this role?"
"Tell me about your education and qualifications."
"What projects are in your GitHub? Walk me through one."
"What's the tech stack for your AI Persona Assistant project?"
"What would you do differently if you rebuilt it?"
"Are you available for a call this week?"
```

---

## Roadmap

- [ ] Streaming responses for lower latency and progressive output
- [ ] Session memory to retain conversation history per user
- [ ] LangGraph integration for richer, graph-based reasoning
- [ ] Multi-resume / multi-profile support

---

## Author

**Brij Patel**
GitHub: [@brij26](https://github.com/brij26)
Live App: [my-vapi-assistant.vercel.app](https://my-vapi-assistant.vercel.app/)
# 🤖 Flaxy — High-Speed AI Chatbot (FastAPI + Groq)

<p align="center">
  <img src="https://img.shields.io/badge/Python-3.12+-3776AB?style=for-the-badge&logo=python&logoColor=white" alt="Python 3.12+" />
  <img src="https://img.shields.io/badge/FastAPI-0.100+-009688?style=for-the-badge&logo=fastapi&logoColor=white" alt="FastAPI" />
  <img src="https://img.shields.io/badge/Groq%20Cloud-Llama%203.3%2070B-F05032?style=for-the-badge&logo=groq&logoColor=white" alt="Groq" />
  <img src="https://img.shields.io/badge/Uvicorn-ASGI-499848?style=for-the-badge&logo=gunicorn&logoColor=white" alt="Uvicorn" />
  <img src="https://img.shields.io/badge/License-MIT-blue.svg?style=for-the-badge" alt="License: MIT" />
</p>

**Flaxy** is a modern, ultra-responsive AI chatbot web application powered by **FastAPI**, **Groq Cloud API** (`llama-3.3-70b-versatile`), and a sleek vanilla **HTML5 / CSS3 / JavaScript** frontend. It features real-time token streaming using `ReadableStream` and server-side `StreamingResponse` for instantaneous, typewriter-style responses.

---

## 🌟 Key Features

- ⚡ **Ultra-Fast Streaming**: Uses asynchronous chunk streaming (`StreamingResponse` + Fetch `ReadableStream`) powered by Groq's high-throughput LPU inference.
- 🧠 **Llama 3.3 70B Versatile**: Utilizes Meta's state-of-the-art open-weights model via Groq Cloud.
- 🎭 **Curated Personality (Flaxy)**: Polite, concise, and structured responses with emoji visual anchors and graceful error recovery defined in `system_prompt.md`.
- 🎨 **Modern Dark Web UI**: Responsive glassmorphic interface with suggestion chips, auto-resizing input, and typing animations.
- 🔒 **Zero Hardcoded Secrets**: Fully environment-variable driven with `.env.example` template and comprehensive `.gitignore`.
- 🛡️ **Graceful Fallbacks**: Clear user notifications if API keys are missing or invalid rather than crashing the server.

---

## 📁 Project Architecture

```text
fastapi-chatbot/
│
├── App/
│   ├── ai/
│   │   ├── base.py              # Abstract base class for AI providers
│   │   └── groq.py              # Groq AsyncGroq implementation & streaming logic
│   └── prompts/
│       └── system_prompt.md     # Flaxy system prompt and behavioral guidelines
│
├── static/
│   ├── index.html               # Chat interface markup
│   ├── script.js                # Frontend streaming & DOM interaction logic
│   └── style.css                # Glassmorphic dark styling & animations
│
├── .env.example                 # Environment configuration template
├── .gitignore                   # Ignores sensitive keys, venv, and cache files
├── main.py                      # FastAPI application entrypoint & routing
├── README.md                    # Project documentation
└── requirements.txt             # Python dependencies
```

---

## 🚀 Getting Started

### 1. Prerequisites

- **Python 3.10+** (Python 3.12 recommended)
- **Groq Cloud API Key**: Sign up and obtain a free API key from [Groq Console](https://console.groq.com/keys).

### 2. Clone the Repository

```bash
git clone https://github.com/Engineer-anand/fastapi-chatbot.git
cd fastapi-chatbot
```

### 3. Set Up Virtual Environment

```bash
# Create virtual environment
python -m venv venv

# Activate virtual environment:
# On Windows (PowerShell):
.\venv\Scripts\Activate.ps1

# On Windows (CMD):
.\venv\Scripts\activate.bat

# On macOS / Linux:
source venv/bin/activate
```

### 4. Install Dependencies

```bash
pip install -r requirements.txt
```

### 5. Configure Environment Variables

Copy the `.env.example` template to `.env`:

```bash
# On Windows (PowerShell):
Copy-Item .env.example .env

# On macOS / Linux:
cp .env.example .env
```

Open `.env` and paste your Groq API key:

```env
GROQ_API_KEY=your_actual_groq_api_key_here
```

---

## 🖥️ Running the Application

Launch the local development server:

```bash
uvicorn main:app --reload
```

Once started, open your browser and go to:

👉 **`http://127.0.0.1:8000`**

---

## 📡 API Endpoints

| Method | Endpoint | Description | Request Body | Response Type |
|---|---|---|---|---|
| `GET` | `/` | Serves the main chatbot web UI | None | `text/html` |
| `POST` | `/chat` | Standard single-turn chat completion | `{"prompt": "Hello"}` | `application/json` |
| `POST` | `/chat/stream` | Real-time token streaming completion | `{"prompt": "Hello"}` | `text/plain; charset=utf-8` |

---

## 🛠️ Tech Stack

- **Backend**: [FastAPI](https://fastapi.tiangolo.com/), [Uvicorn](https://www.uvicorn.org/), [Pydantic v2](https://docs.pydantic.dev/)
- **AI Inference**: [Groq Cloud SDK](https://console.groq.com/) (`llama-3.3-70b-versatile`)
- **Frontend**: HTML5, CSS3 (Custom Glassmorphic design), Vanilla JavaScript (`fetch` + `ReadableStream`)
- **Environment Management**: `python-dotenv`

---

## 📄 License

This project is licensed under the [MIT License](LICENSE).

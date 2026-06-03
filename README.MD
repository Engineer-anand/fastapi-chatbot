# 🤖 Flaxy Chatbot (Groq AI)

Flaxy is a friendly, polite, and responsive AI chatbot built using **FastAPI** for the backend, a clean **HTML/CSS/JavaScript** frontend, and powered by the ultra-fast **Groq API** for intelligent responses.

---

## 🌟 Features

*   **FastAPI Backend:** Lightweight, asynchronous, and high-performance server structure.
*   **Groq Cloud Integration:** Powered by advanced open-source LLMs through Groq for near-instant replies.
*   **Polite Personality:** Built-in system prompting that ensures Flaxy remains helpful, uses fun functional emojis, and gracefully apologizes for any mistakes.
*   **Clean Web UI:** A beautiful and fully responsive static chat interface.

---

## 📁 Project Structure

```text
groq_chatbot/
│
├── App/
│   ├── ai/
│   │   ├── base.py
│   │   └── groq.py
│   └── prompts/
│       └── system_prompt.md
│
├── static/
│   ├── index.html
│   ├── script.js
│   └── style.css
│
├── .env                  # Local Environment Variables (Ignored by Git)
├── .gitignore            # Keeps your secret keys safe
├── main.py               # Application Entry Point
└── requirement.txt       # Dependencies
```

---

## 🚀 Setup & Installation

### 1. Clone the Repository
```bash
git clone https://github.com/Engineer-anand/chatbot.git
cd chatbot
```

### 2. Create a Virtual Environment
```bash
python -m venv venv
# On Windows (PowerShell):
.\venv\Scripts\Activate.ps1
# On Mac/Linux:
source venv/bin/activate
```

### 3. Install Dependencies
```bash
pip install -r requirement.txt
```

### 4. Configure Environment Variables
Create a file named `.env` in the root folder and add your Groq API key:
```env
GROQ_API_KEY=your_actual_groq_api_key_here
```
*(Note: `.env` is automatically ignored by Git to protect your cloud credentials from leaking).*

---

## 🖥️ Running the Application

Start the local FastAPI development server using Uvicorn:
```bash
uvicorn main:app --reload
```

Once the server is running, open your web browser and navigate to:
👉 **`http://127.0.0.1:8000`**

---

## 🛠️ Built With

*   **Python 3.12+**
*   **FastAPI** - Backend Web Framework
*   **Groq SDK** - High-speed AI inference
*   **HTML5 / CSS3 / Vanilla JavaScript** - UI Layout and API calling

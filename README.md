# chatbot-web

A web-based conversational chatbot built with Python and Flask, powered by Groq (Llama 3.1 8B Instant). Features persistent chat history within the session, a clean dark UI, and a minimal codebase designed for clarity and easy extension.

**[Live demo](https://ch-devx-chatbot-web.hf.space/)**

![Demo](/.github/assets/demo.png)

---

## Tech stack

- **Backend:** Python 3.11, Flask, Gunicorn
- **AI:** Groq — Llama 3.1 8B Instant
- **Frontend:** Jinja2 templates, vanilla CSS
- **Session management:** Flask signed cookies (client-side, no database)
- **Hosting:** Hugging Face Spaces (Docker, CPU-Basic)

---

## Project structure
chatbot-web/
├── app.py               # Flask app — routes and Groq API call
├── templates/
│   ├── base.html        # Base layout with shared head and container
│   └── index.html       # Chat UI — message history and input form
├── static/
│   └── style.css        # Dark theme, chat bubble styles
├── Dockerfile           # Container config for Hugging Face Spaces
├── requirements.txt
└── .gitignore

---

## Getting started

### Prerequisites

- Python 3.11 or later
- A Groq API key — get one at [console.groq.com](https://console.groq.com)

### Installation

**1. Clone the repository**

```bash
git clone https://github.com/ch-devx/chatbot-web.git
cd chatbot-web
```

**2. Create and activate a virtual environment**

```bash
# macOS / Linux
python3 -m venv .venv
source .venv/bin/activate

# Windows (PowerShell)
python -m venv .venv
& .venv\Scripts\Activate.ps1
```

**3. Install dependencies**

```bash
pip install -r requirements.txt
```

**4. Configure environment variables**

Create a `.env` file in the project root:

GROQ_API_KEY=your_groq_api_key_here
SECRET_KEY=a_random_secret_string_for_flask_sessions

> The `.env` file is listed in `.gitignore` and will never be committed.

**5. Run the app**

```bash
python app.py
```

Open your browser at `http://127.0.0.1:5000`.

---

## How it works

1. The user submits a message through the input form.
2. Flask appends the message to the session history and calls the Groq API (Llama 3.1 8B Instant).
3. The response is added to the session history and the page re-renders with the full conversation.
4. Clicking **New chat** clears the session and resets the conversation.

---

## Deployment

The app is deployed on [Hugging Face Spaces](https://huggingface.co/spaces) using a Docker container. The `Dockerfile` exposes port `7860` as required by the platform and starts the app with Gunicorn.

To deploy your own instance:

1. Create a new Space on Hugging Face (Docker SDK, public)
2. Push the repository to the Space's git remote or connect it via GitHub sync
3. Add `GROQ_API_KEY` and `SECRET_KEY` as repository secrets under **Settings → Variables and secrets**

---

## Troubleshooting

| Problem | Solution |
|---|---|
| `ModuleNotFoundError: Flask` | Make sure your virtual environment is activated before running. |
| `API key not found` | Confirm your `.env` file exists in the project root with the correct key names. |
| Port already in use | Run with `flask run --port=5001` or stop the process using port 5000. |

---

## License

MIT
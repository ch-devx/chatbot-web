# chatbot-web

A web-based conversational chatbot built with Python and Flask, powered by Google Gemini. Features a persistent chat history within the session, a clean dark UI, and a minimal codebase designed for clarity and easy extension.

---

## Tech stack

- **Backend:** Python 3.8+, Flask
- **AI:** Groq Llama 3.1 8B Instant
- **Frontend:** Jinja2 templates, vanilla CSS
- **Session management:** Flask server-side sessions

---

## Project structure

```
chatbot-web/
├── app.py               # Flask app — routes and Gemini API call
├── templates/
│   ├── base.html        # Base layout with shared head and container
│   └── index.html       # Chat UI — message history and input form
├── static/
│   └── style.css        # Dark theme, chat bubble styles
├── requirements.txt
└── .gitignore
```

---

## Getting started

### Prerequisites

- Python 3.8 or later
- A Gemini API key — get one at [Google AI Studio](https://aistudio.google.com/app/apikey)

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

**4. Configure your API key**

Create a `.env` file in the project root:

```
GEMINI_API_KEY=your_api_key_here
```

> The `.env` file is listed in `.gitignore` and will never be committed.

**5. Run the app**

```bash
python app.py
```

Open your browser at `http://127.0.0.1:5000`.

---

## How it works

1. The user submits a message through the input form.
2. Flask stores the message in the server-side session and calls the Gemini API.
3. The response is appended to the session history and the page re-renders with the full conversation.
4. Clicking **New chat** clears the session and resets the conversation.

---

## Troubleshooting

| Problem | Solution |
|---|---|
| `ModuleNotFoundError: Flask` | Make sure your virtual environment is activated before running. |
| `API key not found` | Confirm your `.env` file exists in the project root with the correct key name. |
| Port already in use | Run with `flask run --port=5001` or stop the process using port 5000. |
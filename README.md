# Chatbot Web

A small learning project that demonstrates a simple web-based chatbot built with Python and Flask. This repository contains a minimal Flask app that renders a web UI and returns responses from a lightweight chat handler — suitable for learning, experimentation, and local development.

**Supported:** basic conversation flow via a web form and simple templating with Jinja2.

---

**Contents**
- **Overview:** quick description of purpose and scope.
- **Getting Started:** how to set up a local environment and run the app.
- **Project Structure:** files and directories in this repo.
- **Usage:** how to interact with the application.
- **Development:** notes for contributors and extension points.
- **Troubleshooting & FAQ**
- **License & Contact**

---

## Overview

`chatbot_web` is a compact learning project that shows how to wire a Flask backend to a simple HTML frontend for conversational interactions. It focuses on clarity and minimal dependencies so you can explore and extend the code easily.

Use cases:
- Learn Flask app structure and templating.
- Prototype simple chat logic or plug in an external NLP/chat service.
- Demonstrate form handling and rendering responses with Jinja2 templates.

## Prerequisites

- Python 3.8 or later installed.
- Basic familiarity with Python and the command line (PowerShell on Windows).

## Getting Started (local)

Open a terminal in the project root and follow these steps.

Create and activate a virtual environment:

```powershell
python -m venv .venv
& .venv\Scripts\Activate.ps1
```

Install dependencies. If a `requirements.txt` exists, use it; otherwise install Flask directly:

```powershell
# If requirements.txt exists
pip install -r requirements.txt

# Otherwise, at minimum install Flask
pip install Flask
```

Set up environment variables:

Create a `.env` file in the project root with your Gemini API key:
GEMINI_API_KEY=your_api_key_here

The app reads this key automatically via `genai.Client()`. You can get a key from [Google AI Studio](https://aistudio.google.com/app/apikey).

Run the application:

```powershell
# Typical options (choose one):
# 1) Run with flask if the app exposes FLASK_APP
$env:FLASK_APP = "app.py"
flask run --host=0.0.0.0 --port=5000

# 2) Or run directly with Python if app.py contains the app.run block
python app.py
```

Open a browser at `http://127.0.0.1:5000` to view the application.

## Project Structure

```
app.py
static/
    style.css
templates/
    index.html
    response.html
README.md
```

- `app.py` — main Flask application entrypoint and routing.
- `templates/` — Jinja2 templates used to render the web UI.
- `static/` — static assets (CSS, images, JS if added).

## How it Works

- The front page (`index.html`) provides a simple form to submit user messages.
- The message is sent to an endpoint in `app.py` which processes the input and returns a response.
- `response.html` is used to render the chatbot reply or to inject it into the page depending on implementation.

This project intentionally keeps the chat logic simple so you can replace or extend it. Example extension points:
- Replace the built-in responder with an external API (OpenAI, local NLP model).
- Add message history and persistent sessions.
- Support AJAX calls for real-time UI updates.

## Development Notes

- Use the virtual environment to isolate dependencies.
- Keep templates small and focused; add modular templates if the UI grows.
- If adding JavaScript for client-side behavior, place files under `static/` and reference them from templates.

Testing locally
- Manual: submit messages through the UI and observe responses.
- Automated testing: add unit tests for chat logic separate from Flask routes.

## Contributing

This is a personal learning project. Feel free to fork it and adapt it to your own use case. Pull requests with improvements or bug fixes are welcome.

## Troubleshooting

- "ModuleNotFoundError: Flask": Ensure your virtual environment is activated and `pip install Flask` was run in that environment.
- Port already in use: change the `--port` option when running `flask run` or stop the process that uses the port.

If an error originates in `app.py`, inspect the traceback in the terminal and check the route handlers for typos or missing imports.

## License

This repository is provided for learning and experimentation. Add a proper license file if you intend to reuse or redistribute code for production use.

## Contact

For questions about this project, open an issue in the repository or make a pull request with suggested improvements.

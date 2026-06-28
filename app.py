from dotenv import load_dotenv
load_dotenv()

from flask import Flask, render_template, request, redirect, url_for, session
from groq import Groq

from werkzeug.middleware.proxy_fix import ProxyFix

import os
import logging

app = Flask(__name__)
app.secret_key = os.getenv("SECRET_KEY", "dev-only-fallback")
app.config.update(
    SESSION_COOKIE_SECURE=True,
    SESSION_COOKIE_SAMESITE="None",
    SESSION_COOKIE_HTTPONLY=True,
)
app.wsgi_app = ProxyFix(app.wsgi_app, x_proto=1, x_host=1)


@app.route("/", methods=["GET"])
def index():
    history = session.get("history", [])
    return render_template("index.html", history=history)


@app.route("/response", methods=["POST"])
def show_response():
    user_input = request.form.get("user_input")
    if not user_input:
        return redirect(url_for("index"))
    history = session.get("history", [])
    response = make_call(user_input, history)
    history.append({"role": "user", "text": user_input})
    history.append({"role": "assistant", "text": response})
    session["history"] = history
    return redirect(url_for("index"))

@app.route("/reset", methods=["GET"])
def reset():
    session.pop("history", None)
    return redirect(url_for("index"))

def make_call(user_input, history=[]):
    try:
        client = Groq(api_key=os.getenv("GROQ_API_KEY"))
        messages = [{"role": m["role"], "content": m["text"]} for m in history]
        messages.append({"role": "user", "content": user_input})
        response = client.chat.completions.create(
            model="llama-3.1-8b-instant",
            messages=messages,
            max_completion_tokens=1024,
        )
        return response.choices[0].message.content
    except Exception as e:
        error_message = getattr(e, "message", None) or str(e)
        logging.error("Groq API error: %s", error_message)
        return "The assistant is temporarily unavailable. Please try again in a moment."


if __name__ == "__main__":
    app.run(debug=True)

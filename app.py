from dotenv import load_dotenv
load_dotenv()

from flask import Flask, render_template, request, redirect, url_for, session
from google import genai

import os

app = Flask(__name__)
app.secret_key = os.getenv("GEMINI_API_KEY", "fallback-only-for-dev")


@app.route("/", methods=["GET"])
def index():
    history = session.get("history", [])
    return render_template("index.html", history=history)


@app.route("/response", methods=["POST"])
def show_response():
    user_input = request.form.get("user_input")
    if not user_input:
        return redirect(url_for("index"))
    response = make_call(user_input)
    history = session.get("history", [])
    history.append({"role": "user", "text": user_input})
    history.append({"role": "assistant", "text": response})
    session["history"] = history
    return redirect(url_for("index"))

@app.route("/reset", methods=["GET"])
def reset():
    session.pop("history", None)
    return redirect(url_for("index"))

def make_call(user_input):
    try:
        client = genai.Client()
        response = client.models.generate_content(
            model="gemini-1.5-flash", contents=user_input
        )
        return response.text
    except Exception as e:
        return f"Error al contactar la API: {e}"


if __name__ == "__main__":
    app.run(debug=True)

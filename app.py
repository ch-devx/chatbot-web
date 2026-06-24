from flask import Flask, render_template, request, redirect, url_for
from google import genai

app = Flask(__name__)
app.secret_key = "dev-secret-key-change-in-production"


@app.route("/", methods=["GET"])
def index():
    history = session.get("history", [])
    return render_template("index.html", history=history)


@app.route("/response", methods=["POST"])
def show_response():
    if request.method == "POST":
        user_input = request.form.get("user_input")
        response = make_call(user_input)
        return render_template(
            "response.html", user_input=user_input, response=response
        )


def make_call(user_input):
    try:
        client = genai.Client()
        response = client.models.generate_content(
            model="gemini-2.5-flash-lite", contents=user_input
        )
        return response.text
    except Exception as e:
        return f"Error al contactar la API: {e}"


if __name__ == "__main__":
    app.run(debug=True)

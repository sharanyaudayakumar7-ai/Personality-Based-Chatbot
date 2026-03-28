from flask import Flask, render_template, request
from personalities import *

app = Flask(__name__)

@app.route("/", methods=["GET", "POST"])
def home():
    response = ""
    emoji = ""

    if request.method == "POST":
        user_input = request.form["user_input"]
        choice = request.form["personality"]

        if choice == "savage":
            response = savage_response(user_input)
            emoji = "💀"
        elif choice == "sweet":
            response = sweet_response(user_input)
            emoji = "💖"
        elif choice == "sarcastic":
            response = sarcastic_response(user_input)
            emoji = "🙄"
        elif choice == "motivational":
            response = motivational_response(user_input)
            emoji = "🚀"

    return render_template("index.html", response=response, emoji=emoji)

if __name__ == "__main__":
    app.run(debug=True)
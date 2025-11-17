from flask import Flask, render_template, session, redirect, request, jsonify
from flask_session import Session
from cs50 import SQL
import logging
from cleaner import *

app = Flask(__name__)

app.config["SESSION_PERMANENT"] = False
app.config["SESSION_TYPE"] = "filesystem"
Session(app)
logger = logging.getLogger(__name__)
logger.setLevel(logging.INFO)

@app.context_processor
def ready():
    if session.get("cancel"):
        x = "cancel"
        return dict(x = x)
    else:
        x = ""
        return dict(x = x)

@app.route("/", methods=["GET", "POST"])
def index():
    if request.method == "POST":
        session["cancel"] = request.json["q"]
        print(session.get("cancel"))
        return jsonify({"msg": "cancel session saved"})
    if not session.get("enter"):
        return redirect("/landing")
    return render_template("index.html", page_id="index")

@app.route("/landing", methods=["GET", "POST"])
def landing():
    if request.method == "POST":
        session["enter"] = request.form.get("name")
        return redirect("/")
    return render_template("landing.html", page_id = "landing")

@app.route("/clean", methods=["GET", "POST"])
def clean():
    if request.method == "POST":
        q = request.json["q"]

        cleaned = clean_query(q)
        return jsonify({"msg": cleaned})
        
@app.route("/recommend", methods=["GET", "POST"])
def recom():
    if request.method == "POST":
        q = request.json["q"]

        recommendation = recommend(q)
        return jsonify({"msg": recommendation})

if __name__ == "__main__":
    app.run(port=5000, debug=True, use_reloader=True, reloader_type="watchdog")
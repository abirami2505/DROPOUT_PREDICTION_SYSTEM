
from flask import Flask, render_template, request, redirect, url_for
import mysql.connector
import pandas as pd
import joblib
import os

app = Flask(__name__)

# ---------------- DATABASE CONNECTION ----------------

db = mysql.connector.connect(
    host="localhost",
    user="root",
    password="abiK@2505",     # put your mysql password here
    database="dropout_system"
)

cursor = db.cursor()

# ---------------- LOAD ML MODEL ----------------

# Build absolute path so it works regardless of where you run the script from
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
model = joblib.load(os.path.join(BASE_DIR, "model", "dropout_model.pkl"))


# ---------------- HOME PAGE ----------------

@app.route("/")
def home():
    return render_template("index.html")


# ---------------- SIGNUP ----------------

@app.route("/signup", methods=["GET","POST"])
def signup():

    if request.method == "POST":

        name = request.form["name"]
        email = request.form["email"]
        password = request.form["password"]

        query = "INSERT INTO counsellor (name,email,password) VALUES (%s,%s,%s)"

        cursor.execute(query,(name,email,password))

        db.commit()

        return redirect("/login")

    return render_template("signup.html")


# ---------------- LOGIN ----------------

@app.route("/login", methods=["GET","POST"])
def login():

    if request.method == "POST":

        email = request.form["email"]
        password = request.form["password"]

        query = "SELECT * FROM counsellor WHERE email=%s AND password=%s"

        cursor.execute(query,(email,password))

        user = cursor.fetchone()

        if user:
            return redirect("/dashboard")
        else:
            return "Invalid Login"

    return render_template("login.html")


# ---------------- DASHBOARD ----------------

@app.route("/dashboard")
def dashboard():
    return render_template("dashboard.html")


# ---------------- DATASET UPLOAD ----------------

@app.route("/upload", methods=["POST"])
def upload():

    file = request.files["file"]

    df = pd.read_csv(file)

    X = df[[
        "attendance_percentage",
        "internal_marks",
        "backlogs",
        "family_income"
    ]]

    predictions = model.predict(X)

    df["risk_level"] = predictions

    results = df.to_dict(orient="records")
    high = 0
    medium = 0
    low = 0

    for r in results:
       if r["risk_level"] == "High":
        high += 1
       elif r["risk_level"] == "Medium":
        medium += 1
       else:
        low += 1

    return render_template("results.html", results=results, high=high, medium=medium, low=low)

    

# ---------------- RUN SERVER ----------------

if __name__ == "__main__":
    app.run(debug=True)
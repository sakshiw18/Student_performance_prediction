from flask import Flask, render_template, request
import joblib
import pandas as pd

app = Flask(__name__)

model = joblib.load("model/model.pkl")
scaler = joblib.load("model/scaler.pkl")

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/predict", methods=["POST"])
def predict():

    gender = float(request.form["gender"])
    race = float(request.form["race"])
    parent = float(request.form["parent"])
    lunch = float(request.form["lunch"])
    prep = float(request.form["prep"])

    features = [[gender, race, parent, lunch, prep]]
    features_scaled = scaler.transform(features)

    prediction = model.predict(features_scaled)[0]
    probability = model.predict_proba(features_scaled)[0][1]

    result = "PASS ✅" if prediction == 1 else "FAIL ❌"

    with open("model/accuracy.txt") as f:
        accuracy = f.read()

    return render_template(
        "result.html",
        result=result,
        probability=round(probability * 100, 2),
        accuracy=accuracy
    )

@app.route("/dashboard")
def dashboard():

    df = pd.read_csv("StudentsPerformance.csv")

    return render_template(
        "dashboard.html",
        avg_math=round(df["math score"].mean(),2),
        avg_reading=round(df["reading score"].mean(),2),
        avg_writing=round(df["writing score"].mean(),2),
        total_students=len(df)
    )

if __name__ == "__main__":
    app.run(debug=True)
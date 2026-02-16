# Student_performance_prediction
Student Performance Prediction System is a Flask-based machine learning web app that predicts whether a student will pass or fail using demographic and academic inputs. It uses a Random Forest Classifier and provides real-time predictions with probability scores and an interactive dashboard for performance analytics.
🎓 Student Performance Prediction System

An end-to-end Machine Learning web application that predicts whether a student will PASS or FAIL based on demographic and academic background factors.

The project integrates data preprocessing, model training, evaluation, and deployment into a fully functional Flask web application with an interactive analytics dashboard.

📌 Project Overview

This project uses a supervised Machine Learning approach to classify student performance.

The system:

Trains a Random Forest Classifier on student data

Evaluates model accuracy

Saves the trained model using Joblib

Deploys it via a Flask web application

Displays predictions with probability scores

Includes a dynamic analytics dashboard using Chart.js

This demonstrates the complete ML lifecycle:
Data → Model → Evaluation → Deployment → Visualization

📂 Dataset

The project uses a structured CSV dataset containing:

Gender

Race/Ethnicity

Parental Level of Education

Lunch Type

Test Preparation Course

Math Score

Reading Score

Writing Score

🎯 Target Variable

A new feature called Average Score is created:

Average = (Math + Reading + Writing) / 3

Students with average ≥ 50 are labeled as:

1 → PASS

0 → FAIL

🛠 Technologies Used

Python

Pandas

Scikit-learn

Flask

HTML

CSS

JavaScript

Chart.js

Joblib

⚙️ Project Structure
project/
│
├── train_model.py
├── app.py
├── StudentsPerformance.csv
│
├── model/
│   ├── model.pkl
│   ├── scaler.pkl
│   └── accuracy.txt
│
├── templates/
│   ├── index.html
│   ├── result.html
│   └── dashboard.html
│
└── static/
    ├── style.css
    └── script.js
🔎 Workflow
1️⃣ Model Training (train_model.py)

Load dataset

Create average score

Encode categorical features

Split into train/test

Apply StandardScaler

Train Random Forest Classifier

Calculate accuracy

Save model + scaler + accuracy

2️⃣ Web Application (app.py)

Load trained model

Accept user input

Scale features

Predict Pass/Fail

Display probability and accuracy

3️⃣ Dashboard

Shows:

Total students

Average Math score

Average Reading score

Average Writing score

Includes:

Bar chart

Line chart

Animated counters

📊 Features

✅ Real-time prediction
✅ Probability score display
✅ Model accuracy display
✅ Interactive analytics dashboard
✅ Clean and responsive UI
✅ Production-ready ML integration

📈 Model Performance

Algorithm: Random Forest Classifier

Evaluation Metric: Accuracy Score

Accuracy is stored and displayed dynamically in the web app

▶️ How to Run Locally
1️⃣ Clone the repository
git clone <your-repo-link>
cd project-folder
2️⃣ Create virtual environment
python -m venv venv
venv\Scripts\activate
3️⃣ Install dependencies
pip install -r requirements.txt
4️⃣ Train the model
python train_model.py
5️⃣ Run the application
python app.py

Open in browser:

http://127.0.0.1:5000/
🚀 Future Improvements

Add database integration

Store prediction history

Add authentication system

Deploy using Docker

Use advanced models (XGBoost, Neural Networks)

Add REST API endpoint

💼 Why This Project Matters

This project demonstrates:

Machine Learning fundamentals

Data preprocessing

Model evaluation

Backend development

Frontend integration

Full deployment workflow

It reflects practical, job-ready ML engineering skills.

import pandas as pd
import os
import joblib
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import LabelEncoder, StandardScaler
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score

# Load dataset
df = pd.read_csv("StudentsPerformance.csv")

# Create average score
df["average"] = (df["math score"] +
                 df["reading score"] +
                 df["writing score"]) / 3

# Target variable
df["result"] = df["average"].apply(lambda x: 1 if x >= 50 else 0)

# Encode categorical columns
le = LabelEncoder()

for col in [
    "gender",
    "race/ethnicity",
    "parental level of education",
    "lunch",
    "test preparation course"
]:
    df[col] = le.fit_transform(df[col])

X = df[[
    "gender",
    "race/ethnicity",
    "parental level of education",
    "lunch",
    "test preparation course"
]]

y = df["result"]

# Split
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42
)

# Scale
scaler = StandardScaler()
X_train = scaler.fit_transform(X_train)
X_test = scaler.transform(X_test)

# Model
model = RandomForestClassifier(n_estimators=200)
model.fit(X_train, y_train)

# Accuracy
accuracy = accuracy_score(y_test, model.predict(X_test))

# Save model
if not os.path.exists("model"):
    os.makedirs("model")

joblib.dump(model, "model/model.pkl")
joblib.dump(scaler, "model/scaler.pkl")

with open("model/accuracy.txt", "w") as f:
    f.write(f"{round(accuracy*100,2)}")

print("Model trained successfully!")
print("Accuracy:", accuracy)
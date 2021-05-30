#!usr/bin/python3

import joblib

model = joblib.load("Salary.pkl")
data = float(input("Enter your experience:"))
prediction = model.predict([[data]])
print(f"You will receive Rs {prediction[0]} approximately...")


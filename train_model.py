import pandas as pd
from sklearn.ensemble import RandomForestClassifier
import joblib

df = pd.read_csv("dataset/synthetic_dataset.csv")

X = df[[
"attendance_percentage",
"internal_marks",
"backlogs",
"family_income"
]]

y = df["dropout_risk"]

model = RandomForestClassifier()

model.fit(X,y)

joblib.dump(model,"model/dropout_model.pkl")

print("Model Trained Successfully")
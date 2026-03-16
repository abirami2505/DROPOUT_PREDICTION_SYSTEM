import pandas as pd
import random

data = []

for i in range(1,1001):
    
    attendance = random.randint(40,100)
    marks = random.randint(30,100)
    backlogs = random.randint(0,5)
    income = random.randint(10000,80000)

    if attendance < 60 or marks < 50 or backlogs >=3:
        risk = "High"
    elif attendance < 75:
        risk = "Medium"
    else:
        risk = "Low"

    data.append([i,attendance,marks,backlogs,income,risk])

df = pd.DataFrame(data,columns=[
"student_id",
"attendance_percentage",
"internal_marks",
"backlogs",
"family_income",
"dropout_risk"
])

df.to_csv("dataset/synthetic_dataset.csv",index=False)

print("Dataset Generated")
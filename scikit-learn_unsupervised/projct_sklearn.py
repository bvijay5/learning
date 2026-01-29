import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from sklearn.preprocessing import LabelEncoder, StandardScaler
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression




data = {
    "StudyHours": [2,5,8,3,7,1,6,4,9,2,5,6,1,3,8,7,4,9,10,2],
    "Attendance": [60,80,90,70,85,50,78,65,95,55,76,88,40,60,92,84,66,97,99,53],
    "PastScore": [40,60,75,50,70,30,68,55,80,35,65,72,25,45,78,69,58,85,90,32],
    "Internet": ["Yes","No","Yes","Yes","No","No","Yes","No","Yes","No","Yes","Yes",
                 "No","No","Yes","Yes","No","Yes","Yes","No"],
    "SleepHours": [5,6,8,5,7,4,6,5,9,4,6,7,3,4,8,7,5,9,10,3],
    "Passed": ["No","Yes","Yes","No","Yes","No","Yes","No","Yes","No","Yes","Yes",
               "No","No","Yes","Yes","No","Yes","Yes","No"]
}

df = pd.DataFrame(data)

print(df.head())
print(df.info())

df_label = df.copy()

le_internet = LabelEncoder()
df_label["Internet"]= le_internet.fit_transform(df["Internet"])

le_passed = LabelEncoder()
df_label["Passed"] = le_passed.fit_transform(df["Passed"])

print(df_label)

features = ['StudyHours', 'Attendance', 'PastScore', 'SleepHours']
ss = StandardScaler()
df_scaled = df_label.copy()
df_scaled[features] = ss.fit_transform(df_label[features])

x = df_scaled[['StudyHours', 'Attendance', 'PastScore', 'SleepHours']]
y = df_scaled['Passed']

x_train, x_test, y_train, y_test = train_test_split(x,y, train_size=0.8, random_state=42)


model = LogisticRegression()
model.fit(x_train, y_train)
y_pred = model.predict(x_test)


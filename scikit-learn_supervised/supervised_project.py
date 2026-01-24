# Student Marks Prediction based on no. of hrs studied
import pandas as pd
import math
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_absolute_error, mean_squared_error

data = {
    "Hours": [1,2,3,4,5,6],
    "Score": [52,57,65,70,75,80]
}

df = pd.DataFrame(data)
X = df[["Hours"]]
y = df["Score"]

model = LinearRegression()
model.fit(X,y)
predicted_score = model.predict(X)

mae = mean_absolute_error(y, predicted_score)
mse = mean_squared_error(y, predicted_score)
rmse = math.sqrt(mse)

# Show Results
print("Mean Absolute Score: ", mae)
print("Mean Squared error score: ", mse)
print("Root mean squared error: ",rmse)

# New prediction
val = float(input("Enter no. of hrs studied: "))
new_pred = model.predict([[val]])[0]
print(new_pred)

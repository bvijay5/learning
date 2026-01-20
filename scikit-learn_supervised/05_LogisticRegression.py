import pandas as pd
from sklearn.linear_model import LogisticRegression


x = [[1],[2],[3],[4],[5]]
y = [0,0,1,1,1]

model = LogisticRegression()
model.fit(x,y)

value = int(input("No. of hrs studied: "))

predicted_val = model.predict([[value]])[0]


print(predicted_val)
# if predicted_val == 1:
#     print("Likely to PASS")

# else:
#     print("Likely to FAIL")


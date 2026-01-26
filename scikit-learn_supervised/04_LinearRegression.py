'''
-> finds patern in old data
-> straight Line
-> y = m*x + c

from sklearn.linear_model import LinearRegression
model = LinearRegression()
model.fit(X,y)
model.predict([[value]])
'''

from sklearn.linear_model import LinearRegression
import pandas as pd

X = [[1],[2],[3],[4],[5]]
y = [40,50,65,75,90]

model = LinearRegression()
model.fit(X,y)

hrs = float(input("No. hrs studies: "))
predicted_marks = model.predict([[hrs]])[0]
print(predicted_marks)



'''
print(model.coef_)          -> m
print(model.intercept_)     -> c
'''

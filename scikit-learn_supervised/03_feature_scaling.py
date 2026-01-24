'''
standard scalar -> normal stanadard variate formula [Z = (X-mean)/varience]

min-max -> scaled = (X - Xmin)/(Xmax - Xmin)

Always Scale only X, no need to scale Y
'''


from sklearn.preprocessing import StandardScaler, MinMaxScaler
from sklearn.model_selection import train_test_split
import pandas as pd


data = {
    "time" : [1,2,3,4,5],
    "test_score" : [40,50,60,70,80]
}

df = pd.DataFrame(data)

standard_scalar = StandardScaler()
standard_scaled = standard_scalar.fit_transform(df)

print(pd.DataFrame(standard_scaled, columns=["time", "test_score"]))
print("\n")

min_max = MinMaxScaler()
min_max_scaled = min_max.fit_transform(df)
print(pd.DataFrame(min_max_scaled, columns=["time", "test_score"]))
print("\n")

X = df[["time"]]
y = df[["test_score"]]

X_train, X_test, y_train, y_test = train_test_split(X,y,test_size=0.2, random_state = 42)

print("X_train:\n",X_train)
print("y_train:\n",y_train)
print("X_test:\n",X_test)
print("y_test:\n",y_test)


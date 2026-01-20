import pandas as pd
from sklearn.preprocessing import StandardScaler, MinMaxScaler
from sklearn.model_selection import train_test_split


data = {
    "hrs": [1,2,3,4,5],
    "marks":[40,50,60,70,80]
}

df = pd.DataFrame(data)

ss = StandardScaler()
Sscaled = ss.fit_transform(df)
print(pd.DataFrame(Sscaled, columns=["hrs", "marks"]))

X = df[["hrs"]]
y = df[["marks"]]

X_train, X_test, y_train, y_test = train_test_split(X,y, test_size=0.2, random_state=42)
import pandas as pd
from sklearn. preprocessing import MinMaxScaler
from sklearn.neighbors import KNeighborsClassifier
from sklearn.model_selection import train_test_split
from sklearn.metrics import classification_report, confusion_matrix

df = pd.read_csv("learning/scikit-learn_supervised/500hits.csv",  encoding='latin-1')

# print(df.head())

df = df.drop(columns=['PLAYER', 'CS'])

X = df.iloc[:, :13]
y = df.iloc[:, 13]

X_train, X_test, y_train, y_test = train_test_split(X,y, test_size=0.2, random_state=11)


scaler = MinMaxScaler(feature_range = (0,1))

X_train = scaler.fit_transform(X_train)
X_test = scaler.fit_transform(X_test)

model = KNeighborsClassifier(n_neighbors=8)
model.fit(X_train, y_train)
y_pred = model.predict(X_test)


print(model.score(X_test, y_test))

cr = classification_report(y_test, y_pred)
print(cr)

cm = confusion_matrix(y_test, y_pred)
print(cm)
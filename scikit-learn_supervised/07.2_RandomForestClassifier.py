import pandas as pd
from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import train_test_split
from sklearn.metrics import classification_report, confusion_matrix

df = pd.read_csv("learning/scikit-learn_supervised/500hits.csv", encoding = 'latin-1')

df = df.drop(columns=["PLAYER", "CS"])

X = df.iloc[:, :13]
y = df.iloc[:, 13]

X_train, X_test, y_train, y_test = train_test_split(X,y, test_size=0.2, random_state=17)

model = RandomForestClassifier(
    n_estimators=1000,
    criterion='entropy',
    min_samples_split=10,
    max_depth=14,
    random_state=42
)
model.fit(X_train, y_train)
y_pred = model.predict(X_test)

print(model.score(X_test, y_test))

cr = classification_report(y_test, y_pred)
print(cr)

cm = confusion_matrix(y_test, y_pred)
print(cm)

print(pd.DataFrame(model.feature_importances_, index=X.columns))
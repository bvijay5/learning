import pandas as pd
from sklearn.tree import DecisionTreeClassifier
from sklearn.model_selection import train_test_split
from sklearn.metrics import confusion_matrix, classification_report

df = pd.read_csv("learning/scikit-learn_supervised/500hits.csv", encoding='latin-1')


df = df.drop(columns=['PLAYER', 'CS'])
# print(df.head())

X = df.iloc[:, 0:13]
y = df.iloc[:, 13]

X_train, X_test, y_train, y_test = train_test_split(X,y, test_size=0.2, random_state=17)


model = DecisionTreeClassifier()
print(model.get_params())   # to know all parameters in model

model = DecisionTreeClassifier(ccp_alpha=0.04, criterion='entropy', random_state=17)
model.fit(X_train, y_train)
y_pred = model.predict(X_test)

cm = confusion_matrix(y_test, y_pred)
print(cm)

cr = classification_report(y_test, y_pred)
print(cr)

print(model.score(X_test, y_test))


# To check how much each column is important
print(pd.DataFrame(model.feature_importances_, index= X.columns))
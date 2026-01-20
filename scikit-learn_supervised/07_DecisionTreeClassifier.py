from sklearn.tree import DecisionTreeClassifier


X = [
    [7,2],
    [8,3],
    [9,8],
    [10,9]
    ]
y = [0,0,1,1]

model = DecisionTreeClassifier()
model.fit(X,y)

s = float(input("Enter size: "))
c = float(input("Enter shade(1-10): "))

predicted_val = model.predict([[s,c]])[0]

if predicted_val == 0:
    print("Most likly APPLE")
else:
    print("Most likely ORANGE")
    
from sklearn.neighbors import KNeighborsClassifier


X = [
    [180,7],
    [200,7.5],
    [250,8],
    [300,8.5],
    [330,9],
    [360,9.5]
]
y = [0,0,0,1,1,1]

model = KNeighborsClassifier(n_neighbors=3)

model.fit(X,y)

gm = float(input("Enter weight in gm: "))
s  = float(input("Enter size in: "))

predicted_val = model.predict([[gm,s]])[0]

if predicted_val == 0:
    print("Most Likly APPLE")

else:
    print("Most likely ORANGE")

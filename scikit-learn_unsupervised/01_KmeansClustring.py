import pandas as pd
import matplotlib.pyplot as plt 
from sklearn.cluster import KMeans

data = {
    "Customer": ["Riya", "Aman", "Vijay", "neha", "Khushaal", "Sneha"],
    "Age": [20,30,40,22,38,25],
    "Spending": [100,200,300,110,290,130]
}


df = pd.DataFrame(data)

X = df[["Age", "Spending"]]

model = KMeans(n_clusters = 2, random_state = 2, n_init=10)

df["Group"] = model.fit_predict(X)

print(df["Group"])

plt.figure(figsize=(6,5))

for group in df["Group"].unique():
    group_data = df[df["Group"]==group]
    plt.scatter(group_data["Age"], group_data["Spending"], label = f"Group {group}")

plt.xlabel("Age")
plt.ylabel("spending")
plt.legend()
plt.grid()
plt.show()

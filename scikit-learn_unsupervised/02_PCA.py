import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from sklearn.preprocessing import StandardScaler
from sklearn.decomposition import PCA


data = {
    'Age': [25, 30, 35, 40, 45, 50],
    'Income': [30000, 40000, 50000, 60000, 70000, 80000],
    'Spending': [70, 60, 50, 40, 30, 20],
    'Savings': [1000, 5000, 8000, 10000, 15000, 20000]
}

df = pd.DataFrame(data)

scaler = StandardScaler()
scaled_data = scaler.fit_transform(df)

pca = PCA(n_components=2)
pca_result = pca.fit_transform(scaled_data)


pca_df = pd.DataFrame(pca_result, columns=["PCA1", "PCA2"])

explained_varience = pca.explained_variance_ratio_
print("Varience Captured by each PCA: ", np.round(explained_varience*100,2))

plt.scatter(pca_df["PCA1"], pca_df["PCA2"])
plt.xlabel("PCA1")
plt.ylabel("PCA2")
plt.title("PCA projection (2D View)")
plt.grid(True)
plt.show()

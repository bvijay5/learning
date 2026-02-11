import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split
from sklearn.svm import SVC


np.random.seed(42)

num_samples = 500

mean1 = 55
std_dev1 = 10

column1_numbers = np.random.normal(mean1, std_dev1, num_samples)
column1_numbers = np.clip(column1_numbers, 30, 120)
column1_numbers = np.round(column1_numbers).astype(int)

mean2 = 18
std_dev2 = 3

column2_numbers = np.random.normal(mean2, std_dev2, num_samples)
column2_numbers = np.clip(column2_numbers, 12, 26)
column2_numbers = np.round(column2_numbers).astype(int)

column3_numbers = np.random.randint(0, 2, size=num_samples)
column3_numbers[column1_numbers > mean1] = 1

data = {
    "Miles_Per_week": column1_numbers,
    "Farthest_run": column2_numbers,
    "Qualified_Boston_Marathon": column3_numbers
}

df = pd.DataFrame(data)


print(df.head())

# for qualified in df['Qualified_Boston_Marathon'].unique():
#     grouped_data = df[df["Qualified_Boston_Marathon"]==qualified]
#     plt.scatter(grouped_data["Miles_Per_week"], grouped_data["Farthest_run"],label = f"Passed {qualified}", alpha=0.5, cmap='coolwarm')

# # plt.scatter(df['Miles_Per_week'], df['Farthest_run'], c = df['Qualified_Boston_Marathon'], cmap='coolwarm', alpha=0.5)

# plt.xlabel("Miles_Per_week")
# plt.ylabel("Farthest_run")
# plt.title("Scatter Plot")
# plt.legend()
# plt.show()

X = df.drop(columns=['Qualified_Boston_Marathon'])
y = df['Qualified_Boston_Marathon']

X_train, X_test, y_train, y_test = train_test_split(X,y, test_size=0.2, random_state=33)


model = SVC()
model.fit(X_train, y_train)
y_pred = model.predict(X_test)

print(model.score(X_test, y_test))

#regularisation
print("Regularisation:")
reg0 = SVC(C = 1000)
reg0.fit(X_train, y_train)
y_pred = reg0.predict(X_test)
print(reg0.score(X_test, y_test))


# gamma
print("gamma:")
gam = SVC(gamma = 1) # can also take any one -> 'auto', 'scale', any number like 0.1
gam.fit(X_train, y_train)
y_pred = gam.predict(X_test)
print(gam.score(X_test, y_test))

#kernal
print("kernal:")
ker = SVC(kernel = 'rbf') # 'linear', 'poly', 'rbf', 'sigmoid', 'precomputed'
ker.fit(X_train, y_train)
y_pred = ker.predict(X_test)
print(ker.score(X_test, y_test))
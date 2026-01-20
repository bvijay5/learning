import pandas as pd

#Series
s = pd.Series([10,20,30], index = ['a','b','c'])

print(s)
print(s['a'])

#DataFrame
data = {
    "name": ["Ram", "Lakshman", "Hanuman"],
    "roll_no": [1,2, 3]
}
df = pd.DataFrame(data)
print(df)

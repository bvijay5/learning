import pandas as pd
from sklearn.compose import make_column_transformer
from sklearn.preprocessing import OneHotEncoder, OrdinalEncoder

d = {
    'sales': [100000,222000,1000000,522000,111111,222222,1111111,20000,75000,90000,1000000,10000],
    'city': ['Tampa','Tampa','Orlando','Jacksonville','Miami','Jacksonville','Miami','Miami',
             'Orlando','Orlando','Orlando','Orlando'],
    'size': ['Small', 'Medium','Large','Large','Small','Medium','Large','Small','Medium','Medium',
             'Medium','Small',]
}

df = pd.DataFrame(d)

ohe = OneHotEncoder(sparse_output=False)
oe = OrdinalEncoder()

ct = make_column_transformer(
    (ohe, ['city']),
    (oe, ['size']),
    remainder='passthrough'
)

ct.set_output(transform='pandas')
print(ct.fit_transform(df))


ct2 = make_column_transformer(
    (ohe, ['city']),
    (oe, ['size']),
    remainder='drop'
)

ct2.set_output(transform='pandas')
print(ct2.fit_transform(df))

ct3 = make_column_transformer(
    (ohe, ['city']),
    ('passthrough', ['size']),
    remainder='drop'
)
ct3.set_output(transform='pandas')
print(ct3.fit_transform(df))

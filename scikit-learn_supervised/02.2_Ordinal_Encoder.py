import pandas as pd
from sklearn.preprocessing import OrdinalEncoder

d = {
    'sales': [100000,222000,1000000,522000,111111,222222,1111111,20000,75000,90000,1000000,10000],
    'city': ['Tampa','Tampa','Orlando','Jacksonville','Miami','Jacksonville','Miami','Miami',
             'Orlando','Orlando','Orlando','Orlando'],
    'size': ['Small', 'Medium','Large','Large','Small','Medium','Large','Small','Medium','Medium',
             'Medium','Small',]
}

df = pd.DataFrame(d)

# print(df['size'].unique())

sizes = ['Small', 'Medium', 'Large']

oe = OrdinalEncoder(categories=[sizes]).set_output(transform="pandas")
df['size'] = oe.fit_transform(df[['size']])
'''
If someday "Extra Large" appears -> error

Best practice:

OrdinalEncoder(
    categories=[sizes],
    handle_unknown='use_encoded_value',
    unknown_value=-1
)
'''

print(df)
import numpy as np
import pandas as pd
from numpy.random import randn, randint

# GroupBy, merging, joining, concatinating

# data = {
#     'Company': ['Goog', 'Goog', 'MSFT', 'MSFT', 'FB', 'FB'],
#     'Person': ['Sam', 'Charlie', 'Amy', 'Van', 'Carl', 'Sarah'],
#     'Sales': [200, 120, 340, 124, 243, 350]
# }

# df = pd.DataFrame(data)
# print(df)
# byCompany = df.groupby('Company')['Sales']
# df1 = byCompany.mean()
# print(df1)
# print(byCompany.sum())
# print(byCompany.sum().loc["FB"])
# print(df.groupby('Company').count())
# print(df.groupby('Company').describe())
# print(df.groupby('Company').describe().transpose())

# df1 = pd.DataFrame(randn(4,4))
# print(df1)
# df2 = pd.DataFrame(randn(4,4))
# print(df2)
# df3 = pd.DataFrame(randn(4,4))
# print(df3)

# print(pd.concat([df1, df2, df3], axis=1))

# df4 = pd.DataFrame(randint(1, 50, (3, 4)))
# print(df4)


# data1 = {
#     "A": ["A0", "A1", "A2"],
#     "B": ["B0", "B1", "B2"],
#     "key": ["K0", "K1", "K2"]
# }

# data2 = {
#     "C": ["C0", "C1", "C2"],
#     "D": ["D0", "D1", "D2"],
#     "key": ["K0", "K1", "K2"]
# }

# left = pd.DataFrame(data1)
# right = pd.DataFrame(data2)
# print(left)
# print(right)

# merge1 = pd.merge(left, right, how='inner', on='key')
# print(merge1)


data1 = {
    "A": ["A0", "A1", "A2"],
    "B": ["B0", "B1", "B2"],
    "key1": ["K0", "K1", "K2"]
}

data2 = {
    "C": ["C0", "C1", "C2"],
    "D": ["D0", "D1", "D2"],
    "key2": ["K0", "K1", "K2"]
}

left = pd.DataFrame(data1)
right = pd.DataFrame(data2)
print(left)
print(right)
merge2 = pd.merge(left, right, on=['key1', 'key2'], how='outer')
print(merge2)
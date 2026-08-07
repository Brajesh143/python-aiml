import numpy as np
import pandas as pd
from numpy.random import randn

# outside = ['G1', 'G1', 'G1', 'G2', 'G2', 'G2']
# inside = [1, 2, 3, 1, 2, 3]
# hier_index = list(zip(outside, inside))
# print(hier_index)
# hier_index = pd.MultiIndex.from_tuples(hier_index)
# print(hier_index)
# df = pd.DataFrame(randn(6, 2), hier_index, ["A", "B"])
# print(df)
# df.index.names = ['Groups', 'Num']
# print(df)

# print(df.xs('G1'))
# print(df.xs('G2'))

# print(df.xs(1, level='Num'))

# Missing Data
d = {'A': [1, 2, np.nan], 'B': [5, np.nan, np.nan], 'C': [1, 2, 3]}
df1 = pd.DataFrame(d)
print(df1)

# print(df1.dropna())
# print(df1.dropna(axis=1))
# print(df1.dropna(thresh=2))
print(df1.fillna(value='FILL_VALUE'))
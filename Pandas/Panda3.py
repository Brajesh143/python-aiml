import numpy as np
import pandas as pd

data = np.random.randn(4, 4)
df1 = pd.DataFrame(
    [[1, 2, 3, 4], [3, 4, 5, 6], [4, 5, 6, 8], [6, 7, 6, 9]], index=["A", "B", "C", "D"], columns=["a", "b", "c", "d"])
print(df1)

# print(df1["c"].unique())

# print(df1["c"].nunique())

# print(df1["c"].value_counts())

# def times2(x):
#     return x * 2

# print(df1["c"].apply(times2))
# print(df1["c"].apply(lambda x: x *2))

# df1.set_index(["x", "y", "z", "p"])
# print(df1)

# print(df1['d'].apply(lambda x : x * 3))

print(df1.sort_values('d'))
# df1.drop('c', axis=1, inplace=True)
# print(df1)
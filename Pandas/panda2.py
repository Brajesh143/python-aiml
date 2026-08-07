import numpy as np
import pandas as pd

# data1 = np.random.randn(4, 4)
# pd1 = pd.DataFrame(data1, ["A", "B", "C", "D"], ["a", "b", "c", "d"])
# print(pd1)
# pd1['E'] = [1, 2, 3, 4]
# print(pd1)
# pd1.drop("c", axis=1, inplace=True)
# print(pd1)

# loc label based indexing
# df = pd.DataFrame({
#     "name": ["Alice", "Bob", "Chet"],
#     "age": [25, 30, 35],
#     "score": [85, 90, 88]
# }, index=["a", "b", "c"])

# print(df)
# print(df.loc["a"])
# print(df.loc[["a", "c"]])
# print(df.loc["a", "age"])
# print(df.loc[["a", "b"], ["name", "age"]])

# print(df.xs('name'))

arrays = [
    ["Math", "Math", "Science", "Science"],
    ["Midterm", "Final", "Midterm", "Final"]
]

tuples = list(zip(*arrays))
index = pd.MultiIndex.from_tuples(tuples, names=["Subject","Exam"])

df = pd.DataFrame([[85, 90, 78, 88],
                   [80, 95, 82, 91]],
                  index=["Alice","Bob"],
                  columns=index)

print(df)

print(df.xs("Math"))
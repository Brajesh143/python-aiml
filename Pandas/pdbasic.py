# Basic pandas

import numpy as np
import pandas as pd

# Series
# s = pd.Series([10, 20, 30], index=["a", "b", "c"], name="scores")
# print(s)
# print(s.values)
# print(s.index)
# print(s['a'])

# s1 = pd.Series(["Brajesh", 29, "Noida"])
# print(s1)
# print(s1.values)
# print(len(s1))

# s2 = pd.Series([2, 3, 4, 5])
# s3 = pd.Series([5, 6, 7, 8])

# print(s2 + s3)


# DataFrame
# df = pd.DataFrame({
#     "name": ["Alice", "Bob", "Chet"],
#     "age": [25, 30, 35],
#     "city": ["Delhi", "Mumbai", "Bengaluru"]
# }, index=["u1", "u2", "u3"])

# print(df)
# print("Shape:", df.shape)   # (rows, cols)
# print("Columns:", df.columns)
# print("Index:", df.index)

# Practice Questions
# Create a Series of 5 temperatures with custom string index.

# sTemp = pd.Series([40, 50, 42, 44, 45], index=["Noida", "Jaipur", "Chd", "Delhi", "Gurugram"])
# print(sTemp)

# Make a DataFrame with columns ["feature1","feature2","label"] for 4 rows.
# df1 = pd.DataFrame({
#     "feature1": ["F1", "F2", "F4", "F4"],
#     "feature2": ["Fe1", "Fe2", "Fe3", "Fe4"],
#     "label": ["One", "Two", "Three", "Four"]
# })
# print(df1)
# print(df1.shape)
# print(df1.columns)

# Convert a Series to a one-column DataFrame and back.
# s1 = pd.Series(["A", "B", "C", "D"])
# print(s1)
# print(type(s1))

# dfS1 = pd.DataFrame(s1, columns=["a"])
# print(dfS1)
# print(type(dfS1))
# print(dfS1.columns)

df2 = pd.DataFrame({
    "name": ["Alice", "Bob", "Chet"],
    "age": [25, 30, 35],
    "city": ["Delhi", "Mumbai", "Bengaluru"]
})

# print(df2)
# print(df2.columns)
# df2["new"] = df2["name"] + df2["city"] # adding a new row
# df2["Address"] = "Noida"
# print(df2)
# print(df2.drop("new", axis=1, inplace=True)) # inplace=True to delete permanently
# print(df2)

print(df2["name"])
print(df2.index)
print(df2.loc[0])
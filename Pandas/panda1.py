import numpy as np
import pandas as pd

# df = pd.DataFrame(range(1, 5), ['A', 'B', 'C', 'D', 'E'], ['W', 'X', 'Y', 'Z'])

# data = {
#     'Name': ['Alice', 'Bob', 'Charlie'],
#     'Age': [25, 30, 35],
#     'City': ['Delhi', 'Mumbai', 'Bangalore']
# }

# df = pd.DataFrame(data)

# data = [['Alice', 25], ['Bob', 30], ['Charlie', 35]]
# df = pd.DataFrame(data, columns=['Name', 'Age'])

# print(df)
# # print(df['Name'])
# # print(df[['Name', 'Age']])

# print(df.loc[0])   # First row by label 
# # print(df.iloc[1]) 

# data = {
#     'Name': ['Alice', 'Bob', 'Charlie', 'David'],
#     'Age': [25, 30, 35, 40],
#     'City': ['Delhi', 'Mumbai', 'Bangalore', 'Chennai'],
#     'Salary': ['200K', '100K', '60K', '50K'],
#     'Department': ['CS', 'EC', 'IT', 'CE']
# }

# df = pd.DataFrame(data)  # Custom row labels
# print(df)

# print(df.loc[0])
# print(df.iloc[0])

# df = pd.DataFrame(data, index=['a', 'b', 'c', 'd'])
# print(df)
# print(df.loc['c'])
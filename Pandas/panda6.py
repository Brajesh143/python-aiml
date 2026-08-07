# Read and right data with excel

import pandas as pd

# df = pd.read_csv("country.csv")

# df.to_csv("country.csv", sheet_name="NewCountry", index=False)

# # df.loc[0]["Name"] = "India"

# print(df.head())       # View first 5 rows
# print(df.shape)  

df1 = pd.read_html("https://www.w3schools.com/html/html_tables.asp")
print(df1[0])
print(df1[0].head())
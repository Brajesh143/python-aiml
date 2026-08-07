import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from sklearn import linear_model
# import os

# # print(os.getcwd())

df = pd.read_csv('homeprices.csv')
# print(df.head())

# matplotlib inline
plt.xlabel('Area(sqft)')
plt.ylabel('Price(US$)')
plt.scatter(df.area, df.price, color='red', marker='+')
# plt.show()

reg = linear_model.LinearRegression()
reg.fit(df[['area']], df.price)

pridicted_price = reg.predict([[5000]])
print(pridicted_price)
# print(reg.coef_)
# print(reg.intercept_)

# print(135.78767123 * 5000 + 180616.43835616432)

d = pd.read_csv('areas.csv')
print(d.head())

p = reg.predict(d)
d['prices'] = p

print(d)
d.to_csv('prediction.csv', index=False)
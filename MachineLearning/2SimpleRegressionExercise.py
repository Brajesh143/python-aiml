import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from sklearn import linear_model

df = pd.read_csv('canada_per_capita_income.csv')

reg = linear_model.LinearRegression()
reg.fit(df[['year']], df.percapitaincome)
predictedPrice = reg.predict([[2020]])
print(predictedPrice)

# Linear regression
import numpy as np
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression

data = {'study_hours': [2,3,4,5,6,7,8,9,10], 'exam_score': [50,60,70,75,80,85,90,92,95]}

feature_data = pd.DataFrame(data)

# feature extraction from data frame
x = feature_data[['study_hours']]
y = feature_data[['exam_score']]

# train test
x_train, x_test, y_train, y_test = train_test_split(x, y, test_size=0.2, random_state=42)

# 

model = LinearRegression()

model.fit(x_train, y_train)

# user input testing
user_input = float(input("Enter number of hours you study:"))
predicted_score = model.predict([[user_input]])

print(predicted_score[0])


import numpy as np
import pandas as pd

# series in pandas

# data = [1, 4, 6, 7, 9]
# seriesData = pd.Series(data, index=['a', 'b', 'c', 'd', 'e'])
# print(seriesData)
# print(seriesData[2])


# data2 = ["Brajesh", "Computer Enginner", 30, "200K"]
# serData2 = pd.Series(data2)
# print(serData2)

# print(serData2[3]) # we can access the series data directly

# print(serData2[0])

# s = pd.Series([10, 20, 30], index=['a', 'b', 'c'])
# print(s)
# print(s[1])

data3 = {"Math": 80, "English": 90, "SST": 70, "SSC": 75}
serData3 = pd.Series(data3)
# print(serData3)

# print(serData3 + 5)
# print(serData3 > 80)

print(serData3.index)
print(serData3.values)
print(serData3.shape)
print(serData3.count())
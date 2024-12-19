import math
import pandas as pd
import matplotlib.pyplot as plt
def calc_sum(x, y):
    return x + y

print(calc_sum(10,20))
print (calc_sum(10,20))

df = pd.read_csv("titanic.csv")
print(df.describe())

df.plot()
plt.show()
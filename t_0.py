# Создать dataFrame на основе файла example.csv
# Построить гистограмму, получить информацию о dataFrame.

import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv("example.csv",sep=";")
print(df)

print(df.info())

df.plot.hist()
plt.show()

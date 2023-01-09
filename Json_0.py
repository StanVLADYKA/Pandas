# На основе файла example.csv создать JSON  с помощью Pandas.
# Получить среднее значение для каждой колонки файла.

import pandas as pd


df = pd.read_csv("example.csv", sep=";")
print(df)
df.to_json("example.json")

data = pd.read_json("example.json")
df = pd.DataFrame(data)


mean = df.mean()
print("mean ---:  ")
print(mean)


# Day 14: Pandas mini project

import pandas as pd

data = {
    "name": ["Ali", "Beka", "Cemal", "Dana", "Eldar"],
    "age": [22, 35, 45, 29, 50],
    "income": [800, 1500, 2000, 1200, 2500]
}

df = pd.DataFrame(data)

print("Таблица данных:")
print(df)

print("\nОбщая информация:")
print(df.info())

print("\nОписание числовых данных:")
print(df.describe())

print("\nЛюди старше 30 лет:")
print(df[df["age"] > 30])

print("\nСредний доход:")
print(df["income"].mean())
print("\nЛюди с доходом выше среднего:")
print(df[df["income"] > df["income"].mean()])

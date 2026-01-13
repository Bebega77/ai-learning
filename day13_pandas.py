# Day 13: Pandas basics

import pandas as pd

data = {
    "name": ["Alex", "Boris", "Cemal"],
    "age": [25, 35, 45],
    "income": [1000, 1500, 2000]
}

df = pd.DataFrame(data)

print(df)
print("\nТолько возраст:")
print(df["age"])

print("\nЛюди старше 30:")
print(df[df["age"] > 30])

print("\nСредний доход:")
print(df["income"].mean())

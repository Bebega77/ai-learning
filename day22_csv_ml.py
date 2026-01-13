# Day 22: ML with CSV data

import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score

# Загружаем CSV
df = pd.read_csv("people.csv")

print("Данные:")
print(df)

# Признаки и цель
X = df[["age", "income"]]
y = df["adult"]

# Делим данные
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.3, random_state=42
)

# Модель
model = LogisticRegression()
model.fit(X_train, y_train)

# Прогноз
y_pred = model.predict(X_test)

# Оценка
accuracy = accuracy_score(y_test, y_pred)

print("Accuracy:", accuracy)

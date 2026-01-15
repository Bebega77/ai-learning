# Day 23: Feature scaling

import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.preprocessing import StandardScaler
from sklearn.metrics import accuracy_score

# Загружаем данные
df = pd.read_csv("people.csv")

X = df[["age", "income"]]
y = df["adult"]

# Делим данные
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.3, random_state=42
)

# Масштабирование
scaler = StandardScaler()
X_train_scaled = scaler.fit_transform(X_train)
X_test_scaled = scaler.transform(X_test)

# Модель
model = LogisticRegression()
model.fit(X_train_scaled, y_train)

# Прогноз
y_pred = model.predict(X_test_scaled)

# Оценка
accuracy = accuracy_score(y_test, y_pred)

print("Accuracy with scaling:", accuracy)

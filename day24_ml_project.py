# Day 24: Mini ML project (adult prediction, FIXED)

import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score, confusion_matrix

# Загружаем данные
df = pd.read_csv("people.csv")

# Признаки и цель
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

# Прогноз на тесте
y_pred = model.predict(X_test_scaled)

# Метрики
accuracy = accuracy_score(y_test, y_pred)
cm = confusion_matrix(y_test, y_pred, labels=[0, 1])

print("Accuracy:", accuracy)
print("Confusion Matrix:")
print(cm)

# ===== ВВОД ПОЛЬЗОВАТЕЛЯ (ИСПРАВЛЕНО) =====

age = int(input("Введите возраст: "))
income = int(input("Введите доход: "))

# ВАЖНО: DataFrame с теми же колонками
new_person_df = pd.DataFrame(
    [[age, income]],
    columns=["age", "income"]
)

new_person_scaled = scaler.transform(new_person_df)
prediction = model.predict(new_person_scaled)

print(
    f"Новый человек ({age} лет, доход {income}):",
    "Взрослый" if prediction[0] == 1 else "Не взрослый"
)

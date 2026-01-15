# Day 30: Final project (Month 1)

import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score, precision_score, recall_score

# 1. Загружаем данные
df = pd.read_csv("people.csv")

# 2. Признаки и цель
X = df[["age", "income"]]
y = df["adult"]

# 3. Делим данные
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.3, random_state=42
)

# 4. Масштабирование
scaler = StandardScaler()
X_train_scaled = scaler.fit_transform(X_train)
X_test_scaled = scaler.transform(X_test)

# 5. Модель (сбалансированная)
model = LogisticRegression(C=1)
model.fit(X_train_scaled, y_train)

# 6. Оценка модели
y_pred = model.predict(X_test_scaled)

accuracy = accuracy_score(y_test, y_pred)
precision = precision_score(y_test, y_pred, zero_division=0)
recall = recall_score(y_test, y_pred, zero_division=0)

print("Model metrics:")
print("Accuracy:", accuracy)
print("Precision:", precision)
print("Recall:", recall)
print("-" * 30)

# ===== ВВОД ПОЛЬЗОВАТЕЛЯ =====

age = int(input("Введите возраст: "))
income = int(input("Введите доход: "))

# 7. Бизнес-правило
if age < 18:
    print(
        f"Новый человек ({age} лет, доход {income}): Не взрослый (по правилу)"
    )
else:
    new_person = pd.DataFrame(
        [[age, income]],
        columns=["age", "income"]
    )

    new_person_scaled = scaler.transform(new_person)
    prediction = model.predict(new_person_scaled)

    print(
        f"Новый человек ({age} лет, доход {income}):",
        "Взрослый" if prediction[0] == 1 else "Не взрослый"
    )

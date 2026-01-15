# Day 25: Hybrid AI (rules + ML)

import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.linear_model import LogisticRegression

# 1. Загружаем данные
df = pd.read_csv("people.csv")

# 2. Разделяем признаки и цель
X = df[["age", "income"]]
y = df["adult"]

# 3. Делим данные на обучение и тест
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.3, random_state=42
)

# 4. Масштабирование
scaler = StandardScaler()
X_train_scaled = scaler.fit_transform(X_train)

# 5. Обучаем модель
model = LogisticRegression()
model.fit(X_train_scaled, y_train)

# ===== ЧАСТЬ С ПОЛЬЗОВАТЕЛЕМ =====

age = int(input("Введите возраст: "))
income = int(input("Введите доход: "))

# 6. ПРАВИЛО (важно!)
if age < 18:
    print(
        f"Новый человек ({age} лет, доход {income}): Не взрослый (по правилу)"
    )
else:
    # 7. ML используется ТОЛЬКО если правило прошло
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

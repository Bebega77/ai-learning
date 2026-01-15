# Day 29: Accuracy vs Precision & Recall

import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import (
    accuracy_score,
    precision_score,
    recall_score,
    confusion_matrix
)

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

# 5. Модель (нормальный баланс)
model = LogisticRegression(C=1)
model.fit(X_train_scaled, y_train)

# 6. Предсказания
y_pred = model.predict(X_test_scaled)

# 7. Метрики
accuracy = accuracy_score(y_test, y_pred)
precision = precision_score(y_test, y_pred, zero_division=0)
recall = recall_score(y_test, y_pred, zero_division=0)
cm = confusion_matrix(y_test, y_pred, labels=[0, 1])

print("Accuracy:", accuracy)
print("Precision:", precision)
print("Recall:", recall)
print("Confusion Matrix:")
print(cm)

# Day 26: Overfitting (переобучение)

import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score

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

# 5. Модель (ОЧЕНЬ СЛАБАЯ регуляризация)
model = LogisticRegression(C=1000)
model.fit(X_train_scaled, y_train)

# 6. Предсказания
train_pred = model.predict(X_train_scaled)
test_pred = model.predict(X_test_scaled)

# 7. Точность
train_accuracy = accuracy_score(y_train, train_pred)
test_accuracy = accuracy_score(y_test, test_pred)

print("Train accuracy:", train_accuracy)
print("Test accuracy:", test_accuracy)

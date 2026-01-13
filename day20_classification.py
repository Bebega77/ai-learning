# Day 20: Binary classification

from sklearn.linear_model import LogisticRegression
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score
import numpy as np

# Данные: возраст -> взрослый (1) / нет (0)
X = np.array([10, 12, 15, 17, 18, 20, 25, 30, 40]).reshape(-1, 1)
y = np.array([0, 0, 0, 0, 1, 1, 1, 1, 1])


# Делим данные
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.25, random_state=42
)

# Модель классификации
model = LogisticRegression()
model.fit(X_train, y_train)

# Прогноз
y_pred = model.predict(X_test)

# Оценка качества
accuracy = accuracy_score(y_test, y_pred)

print("Тестовые возраста:", X_test.flatten())
print("Реальные классы:", y_test)
print("Предсказания:", y_pred)
print("Accuracy:", accuracy)

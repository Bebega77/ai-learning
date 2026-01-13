# Day 21: Confusion Matrix

from sklearn.linear_model import LogisticRegression
from sklearn.model_selection import train_test_split
from sklearn.metrics import confusion_matrix
import numpy as np

# Данные
X = np.array([10, 12, 15, 17, 18, 20, 25, 30, 40]).reshape(-1, 1)
y = np.array([0, 0, 0, 0, 1, 1, 1, 1, 1])

# Делим данные
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.3, random_state=42
)

# Модель
model = LogisticRegression()
model.fit(X_train, y_train)

# Прогноз
y_pred = model.predict(X_test)

# Матрица ошибок
cm = confusion_matrix(y_test, y_pred)

print("Confusion Matrix:")
print(cm)

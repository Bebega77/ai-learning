# Day 19: Train / Test split

from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split
from sklearn.metrics import mean_squared_error, r2_score
import numpy as np

# Данные
X = np.array([20, 25, 30, 35, 40, 45, 50]).reshape(-1, 1)
y = np.array([500, 700, 1000, 1500, 2000, 2300, 2600])

# Делим данные
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.5, random_state=42
)

# Модель
model = LinearRegression()
model.fit(X_train, y_train)

# Прогнозы
y_pred = model.predict(X_test)

# Метрики
mse = mean_squared_error(y_test, y_pred)
r2 = r2_score(y_test, y_pred)

print("Тестовые данные X:", X_test.flatten())
print("Реальные значения y:", y_test)
print("Прогнозы модели:", y_pred)
print("MSE:", mse)
print("R2:", r2)

# Day 18: Model quality metrics

from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error, r2_score
import numpy as np

# Данные
X = np.array([20, 25, 30, 35, 40]).reshape(-1, 1)
y = np.array([500, 700, 1000, 1500, 2000])

# Модель
model = LinearRegression()
model.fit(X, y)

# Прогнозы на тех же данных
y_pred = model.predict(X)

# Метрики
mse = mean_squared_error(y, y_pred)
r2 = r2_score(y, y_pred)

print("MSE:", mse)
print("R2:", r2)

# Day 16: First Machine Learning model

from sklearn.linear_model import LinearRegression
import numpy as np

# Данные: возраст -> доход
X = np.array([20, 25, 30, 35, 40]).reshape(-1, 1)
y = np.array([500, 700, 1000, 1500, 2000])

# Создаём модель
model = LinearRegression()

# Обучаем модель
model.fit(X, y)

# Делаем прогноз
age = 45
predicted_income = model.predict([[age]])

print(f"Прогноз дохода для возраста {age}: {predicted_income[0]:.2f}")

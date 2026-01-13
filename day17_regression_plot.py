# Day 17: Visualizing linear regression

from sklearn.linear_model import LinearRegression
import numpy as np
import matplotlib.pyplot as plt

# Данные
X = np.array([20, 25, 30, 35, 40]).reshape(-1, 1)
y = np.array([400, 800, 1100, 1400, 2100])

# Модель
model = LinearRegression()
model.fit(X, y)

# Предсказания для линии
X_line = np.linspace(20, 40, 100).reshape(-1, 1)
y_line = model.predict(X_line)

# График
plt.scatter(X, y)
plt.plot(X_line, y_line)
plt.xlabel("Возраст")
plt.ylabel("Доход")
plt.title("Линейная регрессия: возраст vs доход")
plt.show()

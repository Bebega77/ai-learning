# Day 12: NumPy basics

import numpy as np

numbers = np.array([10, 20, 30, 40, 50])

print("Массив:", numbers)
print("Тип данных:", type(numbers))

print("Количество элементов:", numbers.size)
print("Минимум:", numbers.min())
print("Максимум:", numbers.max())
print("Среднее:", numbers.mean())
print("Все элементы умноженные на 2:", numbers * 2)

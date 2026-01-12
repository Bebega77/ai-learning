# Day 2: data types, math, logic

name = input("Введите имя: ")
birth_year = int(input("Введите год рождения: "))

current_year = 2026
age = current_year - birth_year

is_adult = age >= 18
years_to_retirement = 65 - age

print("Имя:", name)
print("Возраст:", age)
print("Совершеннолетний:", is_adult)
print("Лет до пенсии:", years_to_retirement)
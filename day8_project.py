# Day 8: mini project - age analysis

ages = []

print("Введите 5 возрастов")

for i in range(5):
    age = int(input("Возраст: "))
    ages.append(age)

print("\nРезультаты анализа:")
print("Все введённые возраста:", ages)
print("Количество людей:", len(ages))
print("Минимальный возраст:", min(ages))
print("Максимальный возраст:", max(ages))
print("Средний возраст:", sum(ages) / len(ages))

for age in ages:
    if age >= 18:
        print(age, "- взрослый")
    else:
        print(age, "- ребёнок")
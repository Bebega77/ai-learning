# Day 10: file to list and analysis

ages = []

file = open("ages.txt", "r")

for line in file:
    line = line.strip()      # убираем \n
    age = int(line)          # превращаем текст в число
    ages.append(age)

file.close()

print("Данные из файла:", ages)
print("Количество:", len(ages))
print("Минимальный:", min(ages))
print("Максимальный:", max(ages))
print("Средний:", sum(ages) / len(ages))

# Day 4: loops for and while

print("Цикл for:")
for i in range(1, 6):
    print("Число:", i)

print("\nЦикл while:")
count = 1
while count <= 5:
    print("Счёт:", count)
    count += 1
numbers = [10, 20, 30, 40, 50]
total = 0
for n in numbers:
    total += n

print("Сумма:", total)

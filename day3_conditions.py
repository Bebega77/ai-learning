# Day 3: conditions if / else

name = input("Введите имя: ")
age = int(input("Введите возраст: "))

if age < 18:
    print(name, "— несовершеннолетний")
elif age < 65:
    print(name, "— взрослый")
else:
    print(name, "— пенсионер")

# Day 9: working with files (write)

file = open("ages.txt", "w")

file.write("20\n")
file.write("30\n")
file.write("40\n")
file.write("50\n")

file.close()

print("Файл ages.txt создан и заполнен")
# Reading data from file

file = open("ages.txt", "r")

content = file.read()

file.close()

print("\nСодержимое файла:")
print(content)

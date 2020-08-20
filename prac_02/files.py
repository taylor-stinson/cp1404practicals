"""
CP1404- Practical 2
Files
"""
# 1:
name = str(input("Enter name: "))
out_file = open("names.txt", "w")
print(name, file=out_file)
out_file.close()

# 2:
in_file = open("names.txt", "r")
name = in_file.read()
print("Your name is {}".format(name))
in_file.close()

# 3:
in_file = open("numbers.txt", "r")
numbers = in_file.readlines()
total = int(numbers[0].strip()) + int(numbers[1].strip())
print(total)
in_file.close()

# 4:
total = 0
in_file = open("numbers.txt", "r")
numbers = in_file.readlines()
for number in numbers:
    number = int(number.strip())
    total += number
print(total)

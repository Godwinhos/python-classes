# simple calculator app
print("Welcome to our calculator app\n\n")
print('''*******************
1. addition
2. subtraction
3. multiplication
4. division
5. exponential
******************************''')
print("enter to number to add")
first_number = input("enter first number: ")
second_number = input("enter second  number: ")
sum = float(first_number) + float(second_number)
print(f" {first_number} + {second_number} = {sum:.2f}\n\n")
print("subtraction")

print("Enter two number to subtract")
first_number = input("enter first number: ")
second_number = input("enter second  number: ")
sub = float(first_number) - float(second_number)
print(f" {first_number} - {second_number} = {sub:.2f}\n\n")

print("number to multiply")
first_number = input("enter first number: ")
second_number = input("enter second  number: ")
mul = float(first_number) * float(second_number)
print(f" {first_number} * {second_number} = {mul:.2f}\n\n")

print("number to divide")
first_number = input("enter first number: ")
second_number = input("enter second  number: ")
div = float(first_number) / float(second_number)
print(f" {first_number} / {second_number} = {div:.2f}\n\n")

print("exponential")
first_number = input("enter first number: ")
second_number = input("enter second  number: ")
exp = float(first_number) ** float(second_number)
print(f" {first_number} ** {second_number} = {exp:.2f}\n\n")

print("floor divistion")
first_number = input("enter first number: ")
second_number = input("enter second  number: ")
floor = float(first_number) //  float(second_number)
print(f" {first_number} // {second_number} = {floor:.2f}\n\n")

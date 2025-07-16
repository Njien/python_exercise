# A simple calculator app
print("***********************************")
print('''1. Addition
2. Multiplication
2. Subtraction
3. Division
******************************************''')

print("Enter two numbers to add")
#prompt user for first number
first_number = input("First number: \n")
#prompt user for second number
second_number = input("Second number: \n")
Sum = float(first_number) + float(second_number)
print(f"{first_number} + {second_number} = {Sum :.2f}")

print("*************MULTIPLICATION*************")
print("Enter two numbers to multiply")
#prompt users for first number
number_one = input("First Number: \n")
#prompt users for second user
number_two = input("Second Number: \n")
multi = float(number_one) * float(number_two)
print(f"{number_one} * {number_two} = {multi :.2f}")

print("************SUBTRACTION***********")

print("Enter two numbers to subtract")
# prompt users for first number
num_one = input("First Number: \n")
#prompt users for second user
num_two = input("Second Number: \n")
sub = float(num_one) - float(num_two)
print(f"{num_one} - {num_two} = {sub :.2f}")
print("**************DIVISION**************")

print("Enter two numbers to Divide")
# prompt users for first number
Number_one = input("First Number: \n")
#prompt users for second user
Number_two = input("Second Number: \n")
divid = float(Number_one) / float(Number_two)
print(f"{Number_one} / {Number_two} = {divid :.2f}") 
print("****************EXPONENTIATION****************")
print("Enter two numbers to exponent")
# prompt users for first number
Num_one = input("First Number: \n")
#prompt users for second user
Num_two = input("Second Number: \n")
expo = float(Num_one) ** float(Num_two)
print(f"{Num_one} ** {Num_two} = {expo :.2f}") 
print("**************************************")

print("************FLOOR DIVISION************")
 
print("Enter two numbers to Floor  Divide")
# prompt users for first number
Number1 = input("First Number: \n")
#prompt users for second user
Number2 = input("Second Number: \n")
floor_divid = float(Number1) // float(Number2)
print(f"{Number1} // {Number2} = {floor_divid :.2f}")


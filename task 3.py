# request = int(input('Please, enter 4 numbers'))
#
# first = request // 1000
# print(first)
#
# second = request // 100 % 10
# print(second)
#
# third = request % 100 // 10
# print(third)
#
# fourth = request % 10
# print(fourth)
#
# print("Lets multiply : " + str(first * second * third * fourth))
try:
    num1 = int(input("First number:\n"))
    num2 = int(input("Second number:\n"))
    print("Enter mathematical operation:")
    act = input(" 1. +\n 2. -\n 3. *\n 4. /\n")
    if act == "+":
        res = num1 + num2
        print(f"{num1} + {num2} = {res}")
    if act == "-":
        res = num1 - num2
        print(f"{num1} - {num2} = {res}")
    if act == "*":
        res = num1 * num2
        print(f"{num1} * {num2} = {res}")
    if act == "/":
        res = num1 / num2
        print(f"{num1} / {num2} = {res}")
    elif act != "+" and act != "-" and act != "*" and act != "/":
        print("Incorrect command!")

except Exception as error:
    print(f"Occurred an error : {error}")
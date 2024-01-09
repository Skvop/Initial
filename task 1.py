# num_1 = int(input("Please, enter 1st number : "))
# num_2 = int(input('Please, enter 2nd number : '))
# num_3 = int(input('Please, enter 3rd number : '))
# material = input('Please, enter 3 numbers through "-" : ')
# material2 = material.split('-')
# material3 = map(int, material2)
# material4 = list(material3)
#
# action = input("Please tell me what operation to do: take out the maximum from the numbers - 'max'; take out the minimum from the numbers - 'min'; or the arithmetic mean - 'mid': ")
# if action == "min":
#     print(min(material4))
# elif action == "max":
#     print(max(material4))
# elif action == "mid":
#     print(sum(material4)/3)
# else:
#     print('Invalid command, please, restart and follow the instruction.')
try:

    day = int(input("Enter the day of the week number"))
    match day:
        case 1:
            print("monday")
        case 2:
            print("tuesday")
        case 3:
            print("wednesday")
        case 4:
            print("thursday")
        case 5:
            print("friday")
        case 6:
            print("saturday")
        case 7:
            print("sunday")
        case _:
            print("Incorrect number")


except Exception as ex:
    print("Error : " + str(ex))
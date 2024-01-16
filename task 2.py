# diagonal_AC = int(input('Please, enter first diagonal length'))
# diagonal_BD = int(input('Please, enter second diagonal length'))
# print('Square of rhombus equals = ' + str((diagonal_AC * diagonal_BD)/2))
# material = int(input('Please, enter number of meters to convert: '))
#
# task = input('You want to convert in "miles","yards" or "inches"?')
# if task == 'miles':
#     print(material*0.00062137)
# elif task == 'yards':
#     print(material*1.0936)
# elif task == 'inches':
#     print(material * 39.370)
# else:
#     print('Not correct request.')
# try:
#     num1 = int(input("First number : "))
#     num2 = int(input("Second number : "))
#
#     if num1 == num2:
#         print(f"{num1} = {num2}")
#     elif num1<num2:
#         print(f"{num1}, {num2}")
#     else:
#         print(f"{num2}, {num1}")
# # except ValueError as error:
# #     raise Exception("Use only integer numbers !")
# except Exception as error:
#     print(f"Error : {error}")
repeat_count = 0

str_enter = input("Enter string: \n")
symb_srch = input("What symbol to search?: \n")

for i in range(len(str_enter)):
    if str_enter[i] == symb_srch :
        repeat_count += 1
print(f"The {symb_srch} symbol repeats {repeat_count} times.")

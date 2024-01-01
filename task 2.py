# diagonal_AC = int(input('Please, enter first diagonal length'))
# diagonal_BD = int(input('Please, enter second diagonal length'))
# print('Square of rhombus equals = ' + str((diagonal_AC * diagonal_BD)/2))
material = int(input('Please, enter number of meters to convert: '))

task = input('You want to convert in "miles","yards" or "inches"?')
if task == 'miles':
    print(material*0.00062137)
elif task == 'yards':
    print(material*1.0936)
elif task == 'inches':
    print(material * 39.370)
else:
    print('Not correct request.')
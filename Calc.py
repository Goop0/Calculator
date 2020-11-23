print('welcome to calc the calculator')
while True:
    print('type 1 for addition       [+]')
    print('type 2 for reduction      [-]')
    print('type 3 for multiplication [*]')
    print('type 4 for division       [/]')
    print('type 5 to turn off        [0]')

    option = int(input('choose between ( 1, 2, 3, 4, 5):'))

    if option == 1:
        numb = float(input('enter first number:'))
        numb2 = float(input('enter second number:'))
        print(f' the answer is {numb + numb2} ')

    elif option == 2:
        print(numb - numb2)

    elif option == 3:
        print(numb * numb2)

    elif option == 4:
        print(numb / numb2)
            
    else:
        print('error!')   
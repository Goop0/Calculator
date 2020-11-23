print('welcome to calc the calculator') # En kalkulator 
while True: #loopen

    print('type 1 for addition       [+]') # meny
    print('type 2 for reduction      [-]')
    print('type 3 for multiplication [*]')
    print('type 4 for division       [/]')
    print('type 5 to turn off        [0]')

    option = int(input('choose between ( 1, 2, 3, 4, 5):')) #ger användaren 5 olika val
    if option == 5: # om val 5 så stängs den av
        print('turning off...')
        exit(1) # avslutar programet 
    else: # om val 1-4 så fortsätter den
        numb = float(input('enter first number:')) # första talet användaren skriver in
        numb2 = float(input('enter second number:')) # andra talet användaren skriver in
        print('\n') # skapar mellan rum så att det blir tydligare att se svaret

    if option == 1: # addition
        print(numb + numb2) # tar första och andra svaret som användaren gav och adderar
        print('\n') # skapar mellan rum så att det blir tydligare att se svaret

    elif option == 2: # subtraktion
        print(numb - numb2) # tar första och andra svaret som användaren gav och subtraherar
        print('\n') # skapar mellan rum så att det blir tydligare att se svaret

    elif option == 3: # multiplikation
        print(numb * numb2) # tar första och andra svaret som användaren gav och multiplicerade 
        print('\n') # skapar mellan rum så att det blir tydligare att se svaret

    elif option == 4: # division
        print(numb / numb2) # tar första och andra svaret som användaren gav och dividerade 
        print('\n') # skapar mellan rum så att det blir tydligare att se svaret

    else: # om anvädaren inte skriver in 1,2,3,4,5 på val frågan så säger programmet error!
        print('error!')
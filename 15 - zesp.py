def kalk():
    a = int(input('Podaj re pierw liczbe: '))
    b = int(input('Podaj im pierw liczbe: '))
    x = int(input('Podaj re drug liczbe: '))
    y = int(input('Podaj im drug liczbe: '))

    print("Twoje pierwsze liczby to: ", a,"+ i *",b)
    print("Twoje drugie liczby to: ", x,"+ i *",y)

    print("Co Chces zrobiz? +,-,*,/")
    akszyn = input("?: ")
    if akszyn == '+':
        print("Wynik to: ", a+x, " + i *",(b+y))
    elif akszyn == '-':
        print("Wynik to: ", a-x, " + i *",(b-y))
    elif akszyn == '*':
        print("Wynik to: ", (a*b) - (y*b), " + i *",(a*y + b*x))
    elif akszyn == '/':
        print("Wynik to: ", (a*x + b*y)/(x**2 + y**2), " + i *",(x*b - a*y)/(x**2 + y**2))
    else:
        print("er... wot?")

    co = input("NEW DATA (Y/N) ?: ")
    if co == 'Y' or co == 'y':
        kalk()
    else:
        exit()
kalk()
from random import randint
def kalk():
    a = int(input('Podaj piewr liczbe: '))
    b = int(input('Podaj drug liczbe: '))
    print("Co Chces zrobiz? +,-,*,/,#,^,x")
    akszyn = input("?: ")
    if akszyn == '+':
        print("Wynik to: ", a+b)
    elif akszyn == '-':
        print("Wynik to: ", a-b)
    elif akszyn == '*':
        print("Wynik to: ", a*b)
    elif akszyn == '/':
        print("Wynik to: ", a/b)
    elif akszyn == '#':
        print("Wynik to: ", a**(1/b))
    elif akszyn == '^':
        print("Wynik to: ", a**b)
    elif akszyn == 'x':
        print("Wynik to: ", randint(a, b))
    else:
        print("er... wot?")

    co = input("NEW DATA (Y/N) ?: ")
    if co == 'Y' or co == 'y':
        kalk()
    else:
        exit()
kalk()
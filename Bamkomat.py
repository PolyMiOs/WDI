def interfejs():
    print("Co Chcesz Zrobić?")
    print("1. Wpłacić")
    print("2. Wypłacić")
    print("3. Sprawdzić")
    print("4. Wyjść")


def bankomat(saldo, pin):
    interfejs()
    akcja = int(input('?: '))
    if akcja == 1:
        pen = input("Podaj PIN: ")
        if pen != pin:
            print("ZLY PIN")
            bankomat(saldo, pin)
        else:
            addd = int(input("Ile wplacasz?: "))
            print("Dziekuje za twoj biznes")
            bankomat(saldo + addd, pin)
    elif akcja == 2:
        pen = input("Podaj PIN: ")
        if pen != pin:
            print("ZLY PIN")
            bankomat(saldo, pin)
        else:
            minusssss = int(input("Ile wyplacasz?: "))
            if minusssss > saldo:
                print("???????NIEMASZTYLEPIENIENDZY")
                bankomat(saldo, pin)
            print("Dziekuje za twoj biznes")
            bankomat(saldo - minusssss, pin)
    elif akcja == 3:
        pen = input("Podaj PIN: ")
        if pen != pin:
            print("ZLY PIN")
            bankomat(saldo, pin)
        else:
            print("Na KONcie mAsz PienIOnŻKUw: ", saldo)
            print("Dziekuje za twoj biznes")
            bankomat(saldo, pin)
    elif akcja == 4:
        print("Dzienki za twoj biznes")
        return 0
    else:
        print("zla akacja")
        bankomat(saldo,pin)

bankomat(700124, '1984')




from random import randint
from tabulate import tabulate


def pizza(n,m,o):
    base = [[[0]*o for _ in range(m)] for _ in range(n)]
    count = [0] * 10000
    for wys in range(n):
        for szer in range(m):
            for dl in range(o):
                el = randint(0,9999)
                base[wys][szer][dl] = el
                count[el] += 1
    print(tabulate(base))
    return count


def histogram(binersy, kaunter):
    for biners in binersy:
        przedzial = 10000 // biners
        sumy = [0] * biners
        for i in range(biners):
            x = 1
            if not i:
                x = 0
            sumy[i] = sum(kaunter[0+i*przedzial+x:(i+1)*przedzial])
        if max(sumy) < 50:
            break
        
        
    for i in range(biners):
        x=1
        if not i:
            x = 0
        sumy[i] = "=" * sumy[i]
        print(f"[{0+i*przedzial+x:^4} - {(i+1)*przedzial}]   {sumy[i]}")


biners = [3,5,10,20,50,100]        
n = int(input("Podaj n: "))
m = int(input("Podaj m: "))
o = int(input("Podaj o: "))

kaunter = pizza(n,m,o)

histogram(biners, kaunter)
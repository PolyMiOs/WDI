from random import randint
from tabulate import tabulate
import matplotlib.pyplot as plt




def pizza(n,m,o):
    base = [[[0]*o for _ in range(m)] for _ in range(n)]
    count = [0] * 10000
    baza = [0] * (m*n*o)
    h = 0
    for wys in range(n):
        for szer in range(m):
            for dl in range(o):
                el = randint(0,9999)
                base[wys][szer][dl] = el
                count[el] += 1
                baza[h] = el
                h += 1
    print(tabulate(base))
    print
    return (count,baza)


def histogram(binersy, kaunter):
    for biners in binersy:
        przedzial = 10000 // biners
        sumy = [0] * biners
        for i in range(biners):
            x = 0
            if 10000%biners == 0 or i:
                x = 1
            sumy[i] = sum(kaunter[0+i*przedzial:(i+1)*(przedzial)-x])
        if max(sumy) < 50:
            break
        
    if max(sumy) > 50:
        raise ValueError
        exit()
    for i in range(biners):
        x=0
        if 10000%biners == 0 or i:
            x = 1
        sumy[i] = "=" * sumy[i]
        print(f"[{0+i*przedzial:^4} - {(i+1)*(przedzial)-x:^4}]   {sumy[i]}")
    return biners
    

def histogramplotlib(M,a):
        
        plt.hist(M, bins=a)
        #plt.show()

biners = [3,5,10,20,50,100]        
n = int(input("Podaj n: "))
m = int(input("Podaj m: "))
o = int(input("Podaj o: "))

kaunter, baza = pizza(n,m,o)

numbins = histogram(biners, kaunter)
histogramplotlib(baza, numbins)
plt.show()
from tabulate import tabulate
def fib(num):
    a, b = 0, 1
    for _ in range(num):
        yield b
        a, b = b, a + b

def nietakladnyprint(tab):
    for rzad in tab:
        print(rzad)


n = int(input("Podaj N: "))
Tablicza = [[0]*n for _ in range(n)]
gen = fib(n**2)
for k in range(n//2):
    for i in range(k,n-(1+k)):
        Tablicza[k][i] = next(gen)
    for i in range(k,n-(1+k)):
        Tablicza[i][n-(1+k)] = next(gen)
    for i in range(n-(1+k),k,-1):
        Tablicza[n-(1+k)][i] = next(gen)
    for i in range(n-(1+k),k,-1):
        Tablicza[i][k] = next(gen)
if n%2 == 1:
    Tablicza[n//2][n//2] = next(gen)

#nietakladnyprint(Tablicza)
print(tabulate(Tablicza))
from random import randint
from tabulate import tabulate
from matplotlib import pyplot

def findnextsmollest
def create_3d(n):
    base = [[[[randint(-100, 100)]*n]for _ in range(n)] for _ in range(n)]
    print(tabulate(base))
    return base

def arrange_3d(cheese):
    n = len(cheese)
    for z in range(n):
        for k in range(n//2):
            
            for i in range(k,n-(1+k)):
                cheese[k][i][z] = 
            for i in range(k,n-(1+k)):
                cheese[i][n-(1+k)][z] = 
            for i in range(n-(1+k),k,-1):
                cheese[n-(1+k)][i][z] = 
            for i in range(n-(1+k),k,-1):
                cheese[i][k][z] = 
        if n%2 == 1:
            cheese[n//2][n//2][z] = next(gen)


create_3d(int(input("Podaj n: ")))
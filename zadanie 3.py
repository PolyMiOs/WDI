name = 'Mikołaj'
age = 19
print(name)
print(age)
a = 5
b = 7
c = 43.8
d = 'Chleb'
e = 'Mój Pies'
print('Chleb')
print('Mój Pies')
print("{:.2f}".format(round(5/7, 2)))

print("{:.2f}".format(round(a/b, 2)),d,e)

f = int(input("Wpisz liczbę: "))
print("Wpisana przez ciebie liczba to: ", f)
g = int(input("Wpisz liczbę: "))
if g < 0 and f < 0:
    print("OBYWIEF MNIEJSZE OD ZERA")
    exit()
elif g < 0:
    #g = abs(g)
    g = -g
elif f < 0:
    #f = abs(f)
    f = -f
# komentarz
print("Suma twoich liczb to: ", f+g)
print("Roznica twoich liczb to: ", f-g)
print("Iloczyn twoich liczb to: ", f*g)
if f*g == 10:
    print("YAY!")

print("Iloraz twoich liczb to: ", f/g)
print("Kwadrat pierwzej z twoich liczb to: ", f**2)
print("kwadrat drugiej z twoich liczb to: ", f**2)
print("Pierwiastek pierwszej z twoich liczb to: ", f**(1/2))
print("Pierwiastek drugiej z twoich liczb to: ", f**(1/2))

'''Koentarz
Hah


aaa
'''
h = int(input("Wpisz liczbę: "))
j = int(input("Wpisz liczbę: "))
if abs(h-j) > 20:
    sr = (h + j) // 2
    for k in range(1,4):
        print(sr+k)
        print(sr-k)
else:
    for i in range(h,j+1):
        print(i)


z = int(input("Wpisz liczbę na choinke: "))
choin = "*"
for i in range(z):
    if i == 0:
        print((z-1)*" " + "X")
    else:
        print((z - (i+1)) * " " + choin)
    choin = choin + "**"
    if i == z-1:
        print(" " * ((len(choin)-2)//2) + 'U')
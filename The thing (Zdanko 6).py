def ladnyprint(A,B):
    n = len(A)
    print(" Zank ----> DecASCII ")
    for i in range(n):
        print(A[i],"---->",B[i])

slow = input("Podaj ciąg znaków: ")
n = len(slow)
start = 0
stop = 0


for i in range(n):
    if slow[i] == '0':
        start = i+1
        break

for i in range(n-1, 1,-1):
    if slow[i] == '0':
        stop = i
        break
        
new_slow = list(set(slow[start:stop]))
if len(new_slow) == 0:
    print("Xera sa kollo siebie / jest 1 zero / zer  ni ma")
    exit()
    
new_slow.sort(reverse=True)
zanki = [ord(new_slow[i]) for i in range(len(new_slow))]

ladnyprint(new_slow, zanki)
if len(new_slow) >=5:
    print("Pionty co do wielkośći decASCII to:", new_slow[4])
else:
    print(";-; Piontke nie ma （πーπ)")


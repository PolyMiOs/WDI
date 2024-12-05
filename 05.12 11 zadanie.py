from itertools import combinations

def gudtroj(a, b, c):
    
    def rondoosi(p1, p2):
        return p1[0] != p2[0] and p1[1] != p2[1]
    
    sides = sorted([
        ((a[0] - b[0])**2 + (a[1] - b[1])**2, a, b),
        ((a[0] - b[0])**2 + (a[1] - b[1])**2, b, c),
        ((a[0] - b[0])**2 + (a[1] - b[1])**2, a, c)
    ])
    
    if sides[0][0] + sides[1][0] == sides[2][0]:
        return rondoosi(*sides[0][1:]) and rondoosi(*sides[1][1:])
    return False

def punktwtrojko(p, a, b, c):
    
    def areja(x1, y1, x2, y2, x3, y3):
        return abs((x1*(y2-y3) + x2*(y3-y1) + x3*(y1-y2)) / 2.0)
    
    ABC = areja(a[0], a[1], b[0], b[1], c[0], c[1])  # Pole ABC
    PBC = areja(p[0], p[1], b[0], b[1], c[0], c[1]) # Pole PBC
    APC = areja(a[0], a[1], p[0], p[1], c[0], c[1]) # Pole APC
    ABp = areja(a[0], a[1], b[0], b[1], p[0], p[1]) # Pole ABP
    
    return ABC == PBC + APC + ABp


def chek(data):

    for a, b, c in combinations(data, 3):
        if gudtroj(a, b, c):
            if all(not punktwtrojko(p, a, b, c) for p in data if p not in {a, b, c}):
                return True
    return False




data = [(0, 0), (3, 3), (6, 0), (2, 2)]
data1 = [(7,5),(13,5),(14,7),(14,6),(12,8)]
data4 = [(17, 4), (30, 7), (17, 23), (29, 29), (17, 11), (25, 30), (30, 5), (11, 4), (27, 22), (21, 15), (23, 15), (26, 20), (11, 28), (30, 17), (25, 12), (25, 9), (15, 11), (21, 27), (17, 20), (18, 17)]
data3 = [(10, 5), (17, 20), (10, 3), (17, 23), (27, 30)]
print(chek(data))
print(chek(data1))
print(chek(data3))

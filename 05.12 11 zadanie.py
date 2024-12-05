from itertools import combinations

def gudtroj(a, b, c):
    def kwadrt(p1, p2):
        return (p1[0] - p2[0])**2 + (p1[1] - p2[1])**2
    
    def rondoosi(p1, p2):
        return p1[0] != p2[0] and p1[1] != p2[1]
    
    sides = sorted([
        (kwadrt(a, b), a, b),
        (kwadrt(b, c), b, c),
        (kwadrt(a, c), a, c)
    ])
    
    if sides[0][0] + sides[1][0] == sides[2][0]:
        return rondoosi(*sides[0][1:]) and rondoosi(*sides[1][1:])
    return False

def punktwtrojko(p, a, b, c):
    
    def area(x1, y1, x2, y2, x3, y3):
        return abs((x1*(y2-y3) + x2*(y3-y1) + x3*(y1-y2)) / 2.0)
    
    ABC = area(a[0], a[1], b[0], b[1], c[0], c[1])  # Pole ABC
    PBC = area(p[0], p[1], b[0], b[1], c[0], c[1]) # Pole PBC
    APC = area(a[0], a[1], p[0], p[1], c[0], c[1]) # Pole APC
    ABp = area(a[0], a[1], b[0], b[1], p[0], p[1]) # Pole ABP
    
    return ABC == PBC + APC + ABp


def chek(data):

    for a, b, c in combinations(data, 3):
        if gudtroj(a, b, c):
            if all(not punktwtrojko(p, a, b, c) for p in data if p not in {a, b, c}):
                return True
    return False

data = [(0, 0), (3, 3), (6, 0), (2, 2)]
data1 = [(7,5),(13,5),(14,7),(14,6),(12,8)]
print(chek(data))
print(chek(data1))

from itertools import combinations

class Point:
    def __init__(self, x: int, y: int):
        self.x = x
        self.y = y

    def distance_squared(self, other):
        return (self.x - other.x) ** 2 + (self.y - other.y) ** 2

class Triangle:
    def __init__(self, a, b, c):
        self.a = a
        self.b = b
        self.c = c

    def is_good(self):
        sides = sorted([
            (self.a.distance_squared(self.b), self.a, self.b),
            (self.b.distance_squared(self.c), self.b, self.c),
            (self.a.distance_squared(self.c), self.a, self.c)
        ])

        def is_axis_aligned(p1, p2):
            return p1.x != p2.x and p1.y != p2.y

        if sides[0][0] + sides[1][0] == sides[2][0]:
            return is_axis_aligned(*sides[0][1:]) and is_axis_aligned(*sides[1][1:])
        return False

    def contains_point(self, p):
        def area(x1, y1, x2, y2, x3, y3):
            return abs((x1 * (y2 - y3) + x2 * (y3 - y1) + x3 * (y1 - y2)) / 2.0)

        total_area = area(self.a.x, self.a.y, self.b.x, self.b.y, self.c.x, self.c.y)
        area1 = area(p.x, p.y, self.b.x, self.b.y, self.c.x, self.c.y)
        area2 = area(self.a.x, self.a.y, p.x, p.y, self.c.x, self.c.y)
        area3 = area(self.a.x, self.a.y, self.b.x, self.b.y, p.x, p.y)

        return total_area == area1 + area2 + area3

def check_good_triangle(points):
    points_objects = [Point(x, y) for x, y in points]

    for a, b, c in combinations(points_objects, 3):
        triangle = Triangle(a, b, c)
        if triangle.is_good():
            if all(not triangle.contains_point(p) for p in points_objects if p not in {a, b, c}):
                return True
    return False

#points = [(0,4),(1,3),('a',7)]
#check_good_triangle(points)

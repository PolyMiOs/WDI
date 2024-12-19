import pytest
from zadanie_1912 import Point, Triangle, check_good_triangle
point_a = Point(0, 0)
point_b = Point(3, 0)
point_c = Point(0, 4)
point_d = Point('de', 4)
def test_equal_areas():
    global point_a, point_b, point_c
    triangle = Triangle(point_a,point_b,point_c)
    point_inside = Point(1, 1)
    assert triangle.contains_point(point_inside) == True

def test_not_equal_distances():
    global point_a, point_b, point_c
    assert point_a.distance_squared(point_b) != point_a.distance_squared(point_c)

def test_invalid_point_input():
    global point_a, point_d
    with pytest.raises(TypeError):
        point_d.distance_squared(point_a)

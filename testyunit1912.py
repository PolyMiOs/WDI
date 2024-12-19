import unittest
from zadanie_1912 import Point, Triangle, check_good_triangle
point_a = Point(0, 0)
point_b = Point(3, 0)
point_c = Point(0, 4)
point_d = Point('iv03', 4)
class TestTriangleMethods(unittest.TestCase):
    global point_c, point_a, point_b, point_d
    def test_equal_areas(self):
        triangle = Triangle(point_a, point_b, point_c)
        point_inside = Point(1, 1)
        self.assertEqual(triangle.contains_point(point_inside), True)

    def test_not_equal_distances(self):
        self.assertNotEqual(point_a.distance_squared(point_b), point_a.distance_squared(point_c))

    def test_invalid_point_input(self):
        with self.assertRaises(TypeError):
            _ = point_c.distance_squared(point_d)
            

if __name__ == '__main__':
    unittest.main()

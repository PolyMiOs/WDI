def pascal_triangle(row, col):
    if col == 0 or col == row:
        return 1
    return pascal_triangle(row - 1, col - 1) + pascal_triangle(row - 1, col)

def pascal(n):
    triangle = []
    for row in range(n):
        current_row = [pascal_triangle(row, col) for col in range(row + 1)]
        triangle.append(current_row)
    for row in triangle:
        print(" ".join(map(str, row)).center(len(triangle[-1]) * 4))




pascal(5)
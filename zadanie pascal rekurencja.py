def rzad(row, col):
    if col == 0 or col == row:
        return 1
    return rzad(row - 1, col - 1) + rzad(row - 1, col)

def pascal(n):
    trkt = []
    for row in range(n):
        current_row = [rzad(row, col) for col in range(row + 1)]
        trkt.append(current_row)
    for row in trkt:
        print(" ".join(map(str, row)).center(len(trkt[-1])*4))




pascal(30)
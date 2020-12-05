import sys

n, m, row, column, k = map(int, sys.stdin.readline().split())
arr = [list(map(int, sys.stdin.readline().split())) for _ in range(n)]
to_do = list(map(int, sys.stdin.readline().split()))
top, bottom, left, right, front, back = 0, 0, 0, 0, 0, 0
for i in to_do:
    if i == 1:
        if column < m - 1:
            column += 1
            top, bottom, left, right, front, back = left, right, bottom, top, front, back
            if arr[row][column] == 0:
                arr[row][column] = bottom
            else:
                bottom = arr[row][column]
                arr[row][column] = 0
            print(top)
    elif i == 2:
        if column > 0:
            column -= 1
            top, bottom, left, right, front, back = right, left, top, bottom, front, back
            if arr[row][column] == 0:
                arr[row][column] = bottom
            else:
                bottom = arr[row][column]
                arr[row][column] = 0
            print(top)
    elif i == 3:
        if row > 0:
            row -= 1
            top, bottom, left, right, front, back = front, back, left, right, bottom, top
            if arr[row][column] == 0:
                arr[row][column] = bottom
            else:
                bottom = arr[row][column]
                arr[row][column] = 0
            print(top)
    elif i == 4:
        if row < n - 1:
            row += 1
            top, bottom, left, right, front, back = back, front, left, right, top, bottom
            if arr[row][column] == 0:
                arr[row][column] = bottom
            else:
                bottom = arr[row][column]
                arr[row][column] = 0
            print(top)
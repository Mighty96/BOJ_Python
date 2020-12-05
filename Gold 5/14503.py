import sys

column, row = map(int, sys.stdin.readline().split())
robot = list(map(int, sys.stdin.readline().split()))
arr = [list(map(int, sys.stdin.readline().split())) for _ in range(column)]
count = 0

while True:
    if arr[robot[0]][robot[1]] == 0:
        arr[robot[0]][robot[1]] = 2
        count += 1
    if arr[robot[0] - 1][robot[1]] != 0 and \
        arr[robot[0] + 1][robot[1]] != 0 and \
        arr[robot[0]][robot[1] + 1] != 0 and \
        arr[robot[0]][robot[1] - 1] != 0:
        if robot[2] == 0:
            if arr[robot[0] + 1][robot[1]] == 1:
                break
            else:
                robot[0] += 1
        elif robot[2] == 1:
            if arr[robot[0]][robot[1] - 1] == 1:
                break
            else:
                robot[1] -= 1
        elif robot[2] == 2:
            if arr[robot[0] - 1][robot[1]] == 1:
                break
            else:
                robot[0] -= 1
        elif robot[2] == 3:
            if arr[robot[0]][robot[1] + 1] == 1:
                break
            else:
                robot[1] += 1
    else:
        if robot[2] == 0:
            robot[2] = 3
            if arr[robot[0]][robot[1] - 1] == 0:
                robot[1] -= 1
        elif robot[2] == 1:
            robot[2] = 0
            if arr[robot[0] - 1][robot[1]] == 0:
                robot[0] -= 1
        elif robot[2] == 2:
            robot[2] = 1
            if arr[robot[0]][robot[1] + 1] == 0:
                robot[1] += 1
        elif robot[2] == 3:
            robot[2] = 2
            if arr[robot[0] + 1][robot[1]] == 0:
                robot[0] += 1

print(count)
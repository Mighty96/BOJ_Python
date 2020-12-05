import sys
sys.setrecursionlimit(100000)

n = int(sys.stdin.readline())
old_arr = [sys.stdin.readline().rstrip() for _ in range(n)]
new_arr = [[0 for _ in range(n)] for _ in range(n)]
count_1 = 0
count_2 = 0


def bfs(row, column, arr):
    visited[row][column] = 1
    if row > 0:
        if visited[row - 1][column] == 0 and arr[row][column] == arr[row - 1][column]:
            bfs(row - 1, column, arr)
    if row < n - 1:
        if visited[row + 1][column] == 0 and arr[row][column] == arr[row + 1][column]:
            bfs(row + 1, column, arr)
    if column > 0:
        if visited[row][column - 1] == 0 and arr[row][column] == arr[row][column - 1]:
            bfs(row, column - 1, arr)
    if column < n - 1:
        if visited[row][column + 1] == 0 and arr[row][column] == arr[row][column + 1]:
            bfs(row, column + 1, arr)


visited = [[0 for _ in range(n)] for _ in range(n)]
for i in range(n):
    for j in range(n):
        if visited[i][j] == 0:
            bfs(i, j, old_arr)
            count_1 += 1
visited = [[0 for _ in range(n)] for _ in range(n)]
for i in range(n):
    for j in range(n):
        if old_arr[i][j] == 'G' or old_arr[i][j] == 'R':
            new_arr[i][j] = 'R'
        else:
            new_arr[i][j] = 'B'

for i in range(n):
    for j in range(n):
        if visited[i][j] == 0:
            bfs(i, j, new_arr)
            count_2 += 1


print(count_1, count_2)
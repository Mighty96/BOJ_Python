import sys

n, k = map(int, sys.stdin.readline().split())
d = [[*map(int, sys.stdin.readline().split())] for _ in range(n)]
backpack = [[0 for _ in range(100001)] for _ in range(n + 1)]

for i in range(1, n + 1):
    for j in range(1, k + 1):
        if j - d[i - 1][0] >= 0:
            backpack[i][j] = max(backpack[i - 1][j], backpack[i - 1][j - d[i - 1][0]] + d[i - 1][1])
        else:
            backpack[i][j] = backpack[i - 1][j]

print(backpack[n][k])
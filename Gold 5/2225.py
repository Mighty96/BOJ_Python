import sys

n, k = map(int, sys.stdin.readline().split())

arr = [[0 for _ in range(k + 1)] for _ in range(n + 1)]
for i in range(n + 1):
    arr[i][1] = 1
for i in range(k + 1):
    arr[0][i] = 1
if k == 1:
    print(1)
else:
    for j in range(2, k + 1):
        for i in range(1, n + 1):
            arr[i][j] = arr[i - 1][j] + arr[i][j - 1]
    result = arr[n][k] % 1000000000
    print(result)
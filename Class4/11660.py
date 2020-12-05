import sys
sys.setrecursionlimit(100000)

num1, num2 = map(int, sys.stdin.readline().split())
arr1 = [list(map(int, sys.stdin.readline().split())) for _ in range(num1)]
arr2 = [list(map(int, sys.stdin.readline().split())) for _ in range(num2)]
arr1_sum = [[0 for _ in range(num1 + 1)] for _ in range(num1 + 1)]
for i in range(1, num1 + 1):
    for j in range(1, num1 + 1):
        arr1_sum[i][j] = arr1[i - 1][j - 1] + arr1_sum[i - 1][j] + arr1_sum[i][j - 1] - arr1_sum[i - 1][j - 1]

for i in range(num2):
    x1, y1, x2, y2 = arr2[i][0], arr2[i][1], arr2[i][2], arr2[i][3]
    print(arr1_sum[x2][y2] - arr1_sum[x1 - 1][y2] - arr1_sum[x2][y1 - 1] + arr1_sum[x1 - 1][y1 - 1])
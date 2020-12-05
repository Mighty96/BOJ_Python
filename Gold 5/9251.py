import sys

str_a = sys.stdin.readline().rstrip()
str_b = sys.stdin.readline().rstrip()
value = [[0 for _ in range(len(str_a) + 1)] for _ in range(len(str_b) + 1)]
for i in range(1, len(str_b) + 1):
    for j in range(1, len(str_a) + 1):
        if str_a[j - 1] == str_b[i - 1]:
            value[i][j] = value[i - 1][j - 1] + 1
        else:
            value[i][j] = max(value[i - 1][j], value[i][j - 1])
print(value[len(str_b)][len(str_a)])
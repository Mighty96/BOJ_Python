import sys

n, m = map(int, sys.stdin.readline().split())
result = 1
for i in range(m):
    result *= (n - i)
for j in range(m):
    result = result // (j + 1)
print(result)
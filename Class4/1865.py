import sys

tc = int(sys.stdin.readline())
inf = 987654321


def bellman_ford(arr, ds):
    ds[1] = 0
    for i in range(n - 1):
        for start, end, weight in line:
            if ds[end] > ds[start] + weight:
                if ds[start] != inf:
                    ds[end] = ds[start] + weight

    for start, end, weight in line:
        if ds[end] > ds[start] + weight:
            return True
    return False

for i in range(tc):
    n, m, w = map(int, sys.stdin.readline().rstrip().split())
    line = []
    for j in range(m):
        a, b, c = map(int, sys.stdin.readline().rstrip().split())
        line.append([a, b, c])
        line.append([b, a, c])
    for j in range(w):
        a, b, c = map(int, sys.stdin.readline().rstrip().split())
        line.append([a, b, -c])
    d = [inf for _ in range(n + 1)]
    if bellman_ford(line, d):
        print('YES')
    else:
        print('NO')




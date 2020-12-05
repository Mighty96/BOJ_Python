import sys

n = int(sys.stdin.readline())
m = int(sys.stdin.readline())
bus = [list(map(int, sys.stdin.readline().rstrip().split())) for _ in range(m)]
cost = [[0 for _ in range(n + 1)] for _ in range(n + 1)]

for i in range(m):
    if cost[bus[i][0]][bus[i][1]] == 0 or cost[bus[i][0]][bus[i][1]] > bus[i][2]:
        cost[bus[i][0]][bus[i][1]] = bus[i][2]

for i in range(1, n + 1):
    for j in range(1, n + 1):
        if i == j:
            continue
        for k in range(1, n + 1):
            if i == k or j == k:
                continue
            if cost[j][k] == 0 or cost[j][k] > cost[j][i] + cost[i][k]:
                if cost[j][i] != 0 and cost[i][k] != 0:
                    cost[j][k] = cost[j][i] + cost[i][k]

for i in range(1, n + 1):
    print(*cost[i][1::])
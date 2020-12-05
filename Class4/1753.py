import sys
import heapq

v, e = map(int, sys.stdin.readline().split())
k = int(sys.stdin.readline())
arr = [list(map(int, sys.stdin.readline().rstrip().split())) for _ in range(e)]
heap = []
INF = 300000000
d = [INF for _ in range(v + 1)]
a = [[] for _ in range(v + 1)]
adj = [[] for _ in range(v + 1)]

for i in range(e):
    a[arr[i][0]].append(arr[i][1])
    adj[arr[i][0]].append(arr[i][2])

d[k] = 0

heapq.heappush(heap, (0, k))

while heap:
    distance, now = heapq.heappop(heap)

    if d[now] < distance:
        continue
    for i in range(len(a[now])):
        if distance + adj[now][i] < d[a[now][i]]:
            d[a[now][i]] = distance + adj[now][i]
            heapq.heappush(heap, (d[a[now][i]], a[now][i]))

for i in range(1, v + 1):
    if d[i] == INF:
        d[i] = 'INF'
    print(d[i])
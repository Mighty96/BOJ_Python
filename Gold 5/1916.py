import sys
import heapq

n = int(sys.stdin.readline())
m = int(sys.stdin.readline())
inf = 1234567891
arr = [[inf for _ in range(n + 1)] for _ in range(n + 1)]
heap = []
d = [inf for _ in range(n + 1)]
for i in range(m):
    temp_start, temp_goal, temp_cost = map(int, sys.stdin.readline().split())
    if arr[temp_start][temp_goal] > temp_cost:
        arr[temp_start][temp_goal] = temp_cost

start, goal = map(int, sys.stdin.readline().split())
d[start] = 0
heapq.heappush(heap, (0, start))
while True:
    temp = heapq.heappop(heap)
    if d[temp[1]] >= temp[0]:
        for j in range(1, n + 1):
            if d[j] > d[temp[1]] + arr[temp[1]][j]:
                d[j] = d[temp[1]] + arr[temp[1]][j]
                heapq.heappush(heap, (d[j], j))
    if len(heap) == 0:
        break

print(d[goal])
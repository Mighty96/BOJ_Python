import sys
import heapq
import copy


def bp(column, row, count, home):
    home[column][row] = 1
    if count == 3:
        bfs(home)
    else:
        for i in range(row, m):
            if home[column][i] == 0:
                bp(column, i, count + 1, home)
                home[column][i] = 0
        if column + 1 != n:
            for i in range(column + 1, n):
                for j in range(m):
                    if home[i][j] == 0:
                        bp(i, j, count + 1, home)
                        home[i][j] = 0


def bfs(a):
    home = copy.deepcopy(a)
    global result
    count = 0
    heap = []
    for i in range(n):
        for j in range(m):
            if home[i][j] == 2:
                heapq.heappush(heap, [i, j])

    while len(heap) != 0:
        now = list(heapq.heappop(heap))
        if now[0] < n - 1 and home[now[0] + 1][now[1]] == 0:
            home[now[0] + 1][now[1]] = 2
            heapq.heappush(heap, [now[0] + 1, now[1]])
        if now[0] > 0 and home[now[0] - 1][now[1]] == 0:
            home[now[0] - 1][now[1]] = 2
            heapq.heappush(heap, [now[0] - 1, now[1]])
        if now[1] < m - 1 and home[now[0]][now[1] + 1] == 0:
            home[now[0]][now[1] + 1] = 2
            heapq.heappush(heap, [now[0], now[1] + 1])
        if now[1] > 0 and home[now[0]][now[1] - 1] == 0:
            home[now[0]][now[1] - 1] = 2
            heapq.heappush(heap, [now[0], now[1] - 1])
    for i in range(n):
        for j in range(m):
            if home[i][j] == 0:
                count += 1
    if count > result:
        result = count


n, m = map(int, sys.stdin.readline().split())
arr = [list(map(int, sys.stdin.readline().split())) for _ in range(n)]
result = 0
for i in range(n):
    for j in range(m):
        if arr[i][j] == 0:
            bp(i, j, 1, arr)
            arr[i][j] = 0
print(result)
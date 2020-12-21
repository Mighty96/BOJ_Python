import sys

n, m = map(int, sys.stdin.readline().split())
visited = [[False for _ in range(m + 2)] for _ in range(n + 2)]
arr = [[1 for _ in range(m + 2)]]
for _ in range(n):
    arr.append([1] + list(map(int, sys.stdin.readline().split())) + [1])
arr.append([1 for _ in range(m + 2)])

x, y, start_x, start_y, goal_x, goal_y = map(int, sys.stdin.readline().split())
queue = [(start_x, start_y, 0)]
visited[start_x][start_y] = True

while True:
    # 불가능
    if not queue:
        print(-1)
        break

    now_x, now_y, count = queue.pop(0)
    print(now_x, now_y, count)

    if (now_x == goal_x) and (now_y == goal_y):
        print(count)
        break

    # 오른쪽으로 이동
    if not visited[now_x][now_y + 1]:
        visited[now_x][now_y + 1] = True
        judge = True
        for i in range(now_x, now_x + x):
            if arr[i][now_y + y] == 1:
                judge = False
                break
        if judge:
            queue.append((now_x, now_y + 1, count + 1))

    # 왼쪽으로 이동
    if not visited[now_x][now_y - 1]:
        visited[now_x][now_y - 1] = True
        judge = True
        for i in range(now_x, now_x + x):
            if arr[i][now_y - 1] == 1:
                judge = False
                break
        if judge:
            queue.append((now_x, now_y - 1, count + 1))

    # 위쪽으로 이동
    if not visited[now_x - 1][now_y]:
        visited[now_x - 1][now_y] = True
        judge = True
        for i in range(now_y, now_y + y):
            if arr[now_x - 1][i] == 1:
                judge = False
                break
        if judge:
            queue.append((now_x - 1, now_y, count + 1))

    # 아래쪽으로 이동
    if not visited[now_x + 1][now_y]:
        visited[now_x + 1][now_y] = True
        judge = True
        for i in range(now_y, now_y + y):
            if arr[now_x + x][i] == 1:
                judge = False
                break
        if judge:
            queue.append((now_x + 1, now_y, count + 1))

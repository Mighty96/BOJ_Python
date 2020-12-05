from collections import deque
import sys

n, m = map(int, sys.stdin.readline().split())
least_time = [100000] * 200001


def bfs(subin):
    queue = deque([subin])
    least_time[subin] = 0

    while queue:
        v = queue.popleft()
        if v < m and least_time[v * 2] > least_time[v]:
            least_time[v * 2] = least_time[v]
            queue.append(v * 2)
        if v < m and least_time[v + 1] > least_time[v] + 1:
            least_time[v + 1] = least_time[v] + 1
            queue.append(v + 1)
        if v > 0 and least_time[v - 1] > least_time[v] + 1:
            least_time[v - 1] = least_time[v] + 1
            queue.append(v - 1)


def main():
    bfs(n)
    print(least_time[m])

main()
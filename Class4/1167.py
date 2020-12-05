import sys
v = int(sys.stdin.readline())

arr = [list(map(int, sys.stdin.readline().rstrip().split())) for _ in range(v)]
arr.sort()
d = [0] * (v + 1)
result = 0
point = 0
visit = []


def dfs(now, diameter, visit, arr):
    global result
    global point
    visit.append(now)
    for i in range((len(arr[now - 1]) - 2) // 2):
        if not arr[now - 1][(i * 2) + 1] in visit:
            dfs(arr[now - 1][(i * 2) + 1], diameter + arr[now - 1][(i * 2) + 2], visit, arr)
    visit.pop()
    if diameter > result:
        point = now
        result = diameter


def main():
    dfs(arr[0][0], 0, visit, arr)
    dfs(point, 0, visit, arr)
    print(result)


main()

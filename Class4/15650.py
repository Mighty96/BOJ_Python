import sys

n, m = map(int, sys.stdin.readline().split())
number = list(map(int, sys.stdin.readline().split()))
check_list = [False] * n
arr = []
number.sort()


def dfs(cnt):
    if cnt == m:
        print(*arr)
    elif cnt < m:
        for i in range(n):
            if check_list[i]:
                continue

            check_list[i] = True
            arr.append(number[i])
            dfs(cnt + 1)
            arr.pop()
            check_list[i] = False


def main():
    dfs(0)


main()
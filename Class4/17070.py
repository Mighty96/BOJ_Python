import sys

n = int(sys.stdin.readline())
wall = list(range(n))
for i in range(n):
    wall[i] = list(map(int, sys.stdin.readline().split()))

gall_row = len(wall) - 1
gall_column = len(wall[0]) - 1
result = 0


def dfs_a(now_row, now_column):
    global result
    if now_row == gall_row and now_column == gall_column:
        result += 1
    else:
        if now_column < gall_column and wall[now_row][now_column + 1] != 1:
            dfs_a(now_row, now_column + 1)
        if now_row < gall_row and now_column < gall_column and \
                wall[now_row + 1][now_column] != 1 and \
                wall[now_row][now_column + 1] != 1 and \
                wall[now_row + 1][now_column + 1] != 1:
            dfs_b(now_row + 1, now_column + 1)


def dfs_b(now_row, now_column):
    global result
    if now_row == gall_row and now_column == gall_column:
        result += 1
    else:
        if now_column < gall_column and wall[now_row][now_column + 1] != 1:
            dfs_a(now_row, now_column + 1)
        if now_row < gall_row and wall[now_row + 1][now_column] != 1:
            dfs_c(now_row + 1, now_column)
        if now_row < gall_row and now_column < gall_column and \
                wall[now_row + 1][now_column] != 1 and \
                wall[now_row][now_column + 1] != 1 and \
                wall[now_row + 1][now_column + 1] != 1:
            dfs_b(now_row + 1, now_column + 1)


def dfs_c(now_row, now_column):
    global result
    if now_row == gall_row and now_column == gall_column:
        result += 1
    else:
        if now_row < gall_row and wall[now_row + 1][now_column] != 1:
            dfs_c(now_row + 1, now_column)
        if now_row < gall_row and now_column < gall_column and \
                wall[now_row + 1][now_column] != 1 and \
                wall[now_row][now_column + 1] != 1 and \
                wall[now_row + 1][now_column + 1] != 1:
            dfs_b(now_row + 1, now_column + 1)


def main():
    now_row = 0
    now_column = 0

    dfs_a(now_row, now_column + 1)
    print(result)


main()
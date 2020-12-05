import sys

n, m = map(int, sys.stdin.readline().split())
arr = [list(map(int, sys.stdin.readline().split())) for _ in range(n)]


def type_0(row, column): # ㅡ형 0도
    value = 0
    for i in range(row):
        for j in range(column - 3):
            if value < arr[i][j] + arr[i][j + 1] + arr[i][j + 2] + arr[i][j + 3]:
                value = arr[i][j] + arr[i][j + 1] + arr[i][j + 2] + arr[i][j + 3]
    return value


def type_1(row, column): # ㅡ형 90도
    value = 0
    for i in range(row - 3):
        for j in range(column):
            if value < arr[i][j] + arr[i + 1][j] + arr[i + 2][j] + arr[i + 3][j]:
                value = arr[i][j] + arr[i + 1][j] + arr[i + 2][j] + arr[i + 3][j]
    return value


def type_2(row, column): # 사각형
    value = 0
    for i in range(row - 1):
        for j in range(column - 1):
            if value < arr[i][j] + arr[i + 1][j] + arr[i][j + 1] + arr[i + 1][j + 1]:
                value = arr[i][j] + arr[i + 1][j] + arr[i][j + 1] + arr[i + 1][j + 1]
    return value


def type_3(row, column): # ㄴ형 0도
    value = 0
    for i in range(row - 2):
        for j in range(column - 1):
            if value < arr[i][j] + arr[i + 1][j] + arr[i + 2][j] + arr[i + 2][j + 1]:
                value = arr[i][j] + arr[i + 1][j] + arr[i + 2][j] + arr[i + 2][j + 1]
    return value


def type_4(row, column): # ㄴ형 90도
    value = 0
    for i in range(row - 1):
        for j in range(column - 2):
            if value < arr[i][j] + arr[i][j + 1] + arr[i][j + 2] + arr[i + 1][j]:
                value = arr[i][j] + arr[i][j + 1] + arr[i][j + 2] + arr[i + 1][j]
    return value


def type_5(row, column): # ㄴ형 180도
    value = 0
    for i in range(row - 2):
        for j in range(column - 1):
            if value < arr[i][j] + arr[i][j + 1] + arr[i + 1][j + 1] + arr[i + 2][j + 1]:
                value = arr[i][j] + arr[i][j + 1] + arr[i + 1][j + 1] + arr[i + 2][j + 1]
    return value


def type_6(row, column): # ㄴ형 270도
    value = 0
    for i in range(row - 1):
        for j in range(column - 2):
            if value < arr[i][j + 2] + arr[i + 1][j] + arr[i + 1][j + 1] + arr[i + 1][j + 2]:
                value = arr[i][j + 2] + arr[i + 1][j] + arr[i + 1][j + 1] + arr[i + 1][j + 2]
    return value


def type_7(row, column): # ㄹ형 0도
    value = 0
    for i in range(row - 2):
        for j in range(column - 1):
            if value < arr[i][j] + arr[i + 1][j] + arr[i + 1][j + 1] + arr[i + 2][j + 1]:
                value = arr[i][j] + arr[i + 1][j] + arr[i + 1][j + 1] + arr[i + 2][j + 1]
    return value


def type_8(row, column): # ㄹ형 90도
    value = 0
    for i in range(row - 1):
        for j in range(column - 2):
            if value < arr[i][j + 1] + arr[i][j + 2] + arr[i + 1][j] + arr[i + 1][j + 1]:
                value = arr[i][j + 1] + arr[i][j + 2] + arr[i + 1][j] + arr[i + 1][j + 1]
    return value


def type_9(row, column): # ㅏ형 0도
    value = 0
    for i in range(row - 2):
        for j in range(column - 1):
            if value < arr[i][j] + arr[i + 1][j] + arr[i + 1][j + 1] + arr[i + 2][j]:
                value = arr[i][j] + arr[i + 1][j] + arr[i + 1][j + 1] + arr[i + 2][j]
    return value


def type_10(row, column): # ㅏ형 90도
    value = 0
    for i in range(row - 1):
        for j in range(column - 2):
            if value < arr[i][j] + arr[i][j + 1] + arr[i][j + 2] + arr[i + 1][j + 1]:
                value = arr[i][j] + arr[i][j + 1] + arr[i][j + 2] + arr[i + 1][j + 1]
    return value


def type_11(row, column): # ㅏ형 180도
    value = 0
    for i in range(row - 2):
        for j in range(column - 1):
            if value < arr[i + 1][j] + arr[i][j + 1] + arr[i + 1][j + 1] + arr[i + 2][j + 1]:
                value = arr[i + 1][j] + arr[i][j + 1] + arr[i + 1][j + 1] + arr[i + 2][j + 1]
    return value


def type_12(row, column): # ㅏ형 270도
    value = 0
    for i in range(row - 1):
        for j in range(column - 2):
            if value < arr[i][j + 1] + arr[i + 1][j] + arr[i + 1][j + 1] + arr[i + 1][j + 2]:
                value = arr[i][j + 1] + arr[i + 1][j] + arr[i + 1][j + 1] + arr[i + 1][j + 2]
    return value


def type_13(row, column): # ㄴ형 대칭 0도
    value = 0
    for i in range(row - 2):
        for j in range(column - 1):
            if value < arr[i][j + 1] + arr[i + 1][j + 1] + arr[i + 2][j] + arr[i + 2][j + 1]:
                value = arr[i][j + 1] + arr[i + 1][j + 1] + arr[i + 2][j] + arr[i + 2][j + 1]
    return value


def type_14(row, column): # ㄴ형 대칭 90도
    value = 0
    for i in range(row - 1):
        for j in range(column - 2):
            if value < arr[i][j] + arr[i + 1][j] + arr[i + 1][j + 1] + arr[i + 1][j + 2]:
                value = arr[i][j] + arr[i + 1][j] + arr[i + 1][j + 1] + arr[i + 1][j + 2]
    return value


def type_15(row, column): # ㄴ형 대칭 180도
    value = 0
    for i in range(row - 2):
        for j in range(column - 1):
            if value < arr[i][j] + arr[i][j + 1] + arr[i + 1][j] + arr[i + 2][j]:
                value = arr[i][j] + arr[i][j + 1] + arr[i + 1][j] + arr[i + 2][j]
    return value

def type_16(row, column): # ㄴ형 대칭 270도
    value = 0
    for i in range(row - 1):
        for j in range(column - 2):
            if value < arr[i][j] + arr[i][j + 1] + arr[i][j  + 2] + arr[i + 1][j + 2]:
                value = arr[i][j] + arr[i][j + 1] + arr[i][j  + 2] + arr[i + 1][j + 2]
    return value


def type_17(row, column): # ㄹ형 대칭 0도
    value = 0
    for i in range(row - 2):
        for j in range(column - 1):
            if value < arr[i][j + 1] + arr[i + 1][j] + arr[i + 1][j + 1] + arr[i + 2][j]:
                value = arr[i][j + 1] + arr[i + 1][j] + arr[i + 1][j + 1] + arr[i + 2][j]
    return value


def type_18(row, column): # ㄹ형 대칭 90도
    value = 0
    for i in range(row - 1):
        for j in range(column - 2):
            if value < arr[i][j] + arr[i][j + 1] + arr[i + 1][j + 1] + arr[i + 1][j + 2]:
                value = arr[i][j] + arr[i][j + 1] + arr[i + 1][j + 1] + arr[i + 1][j + 2]
    return value


print(max(type_0(n, m), type_1(n, m), type_2(n, m), type_3(n, m),
          type_4(n, m), type_5(n, m), type_6(n, m), type_7(n, m),
          type_8(n, m), type_9(n, m), type_10(n, m), type_11(n, m),
          type_12(n, m), type_13(n, m), type_14(n, m), type_15(n, m),
          type_16(n, m), type_17(n, m), type_18(n, m)))




import sys
n, m = map(int, sys.stdin.readline().split())
arr = [list(map(int, sys.stdin.readline().split())) for _ in range(n)]
chicken = []
house = []
new_chicken = []
result = 987654321


def dfs(new_chicken, gall, count, now):
    if count == gall:
        closed()
    else:
        for i in range(now, min(len(chicken) - m + now + 1, len(chicken))):
            new_chicken.append([chicken[i][0], chicken[i][1]])
            dfs(new_chicken, gall, count + 1, i + 1)
            new_chicken.pop()
    return


def closed():
    global result
    distance = 0
    for i in range(len(house)):
        temp_2 = 987654321
        for j in range(len(new_chicken)):
            temp_1 = abs(house[i][0] - new_chicken[j][0]) + abs(house[i][1] - new_chicken[j][1])
            if temp_1 < temp_2:
                temp_2 = temp_1
        distance += temp_2
    if result > distance:
        result = distance


for i in range(n):
    for j in range(n):
        if arr[i][j] == 1:
            house.append([i, j])
        if arr[i][j] == 2:
            chicken.append([i, j])

if m == len(chicken):
    new_chicken = chicken
    closed()
else:
    for i in range(len(chicken) - m + 1):
        new_chicken.append([chicken[i][0], chicken[i][1]])
        dfs(new_chicken, m, 1, i + 1)
        new_chicken.pop()

print(result)
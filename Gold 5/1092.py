import sys

n = int(sys.stdin.readline())
crane = list(map(int, sys.stdin.readline().split()))
m = int(sys.stdin.readline())
box = list(map(int, sys.stdin.readline().split()))
checked = [False for _ in range(m)]
positive = [0 for _ in range(n)]
time = 0
count = 0


crane.sort(reverse=True)
box.sort(reverse=True)

if box[0] > crane[0]:
    print(-1)
    exit()

while count < m:
    for i in range(n):
        while positive[i] < len(box):
            if crane[i] >= box[positive[i]] and checked[positive[i]] == False:
                checked[positive[i]] = True
                count += 1
                positive[i] += 1
                break
            positive[i] += 1
    time += 1

print(time)
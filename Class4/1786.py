import sys

t = sys.stdin.readline().replace('\n', '')
p = sys.stdin.readline().replace('\n', '')
p_stop = [0 for _ in range(len(p) + 2)]
output = []
t_now = 0
p_now = 0
count = 0


def find(t_start, p_start):
    global count
    if t[t_start:t_start + len(p) - p_start] == p[p_start::]:
        count += 1
        output.append(t_start + 1 - p_start)
        return len(p) + 1
    for i in range(len(p) - p_start):
        if t[t_start + i] != p[p_start + i]:
            return i + 1


temp = 0
for i in range(1, len(p)):
    while temp > 0 and p[i] != p[temp]:
        temp = p_stop[temp - 1]
    if p[i] == p[temp]:
        temp += 1
        p_stop[i + 2] = temp

while t_now + len(p) - p_now <= len(t):
    finished = find(t_now, p_now)
    if p_stop[finished] == 0:
        t_now += 1
        p_now = 0
    else:
        t_now += p_stop[finished]
        p_now = p_stop[finished]

print(count)
for i in output:
    print(i)
import sys

consonant = {'b', 'c', 'd', 'f', 'g', 'h', 'j', 'k', 'l', 'm', 'n', 'p', 'q', 'r', 's', 't', 'v', 'w', 'x', 'y', 'z'}
vowel = {'a', 'e', 'i', 'o', 'u'}

l, c = map(int, sys.stdin.readline().rstrip().split())
sentence = list(map(str, sys.stdin.readline().rstrip().split()))

consonant_list = []
vowel_list = []
output = []


def dfs(word, count, now):
    if count == l:
        output.append(word)
        return

    for i in range(now, len(new_list)):
        word += new_list[i]
        dfs(word, count + 1, i + 1)
        word = word[:-1]
    return


for i in sentence:
    if i in consonant:
        consonant_list.append(i)
    else:
        vowel_list.append(i)
if len(consonant_list) < 2:
    exit()
if len(vowel_list) < 1:
    exit()
consonant_list.sort()
vowel_list.sort()
for i in range(len(vowel_list)):
    for j in range(len(consonant_list) - 1):
        for k in range(j + 1, len(consonant_list)):
            word = consonant_list[j] + consonant_list[k] + vowel_list[i]
            count = 3
            new_list = consonant_list[k + 1:] + vowel_list[i + 1:]
            dfs(word, count, 0)
for i in range(len(output)):
    output[i] = sorted(output[i])
output.sort()

for i in range(len(output)):
    for j in range(l):
        print(output[i][j], end='')
    print()
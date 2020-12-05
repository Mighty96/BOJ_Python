import sys

string = sys.stdin.readline().rstrip()
output = []
prior = {'*': 2, '/': 2, '+': 1, '-': 1, '(': 0}
for i in '('+string+')':
    if i.isalpha():
        print(i, end='')
    elif i == '(':
        output.append(i)
    elif i == ')':
        while True:
            judge = output.pop()
            if judge == '(':
                break
            print(judge, end='')
    else:
        while output[-1] != '(' and prior[i] <= prior[output[-1]]:
            print(output.pop(), end='')
        output.append(i)
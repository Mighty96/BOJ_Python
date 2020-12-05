import sys

n = int(sys.stdin.readline())
k = int(sys.stdin.readline())   # 사과의 갯수
apple = [list(map(int, sys.stdin.readline().split())) for _ in range(k)]
l = int(sys.stdin.readline())   # 방향 변환 횟수
change = []
for i in range(l):
    temp = sys.stdin.readline().rstrip().split()
    change.append([int(temp[0]), temp[1]])

board = [[0 for _ in range(n + 2)] for _ in range(n + 2)]
for i in range(n + 2):
    board[i][0] = 1
    board[i][n + 1] = 1
    board[0][i] = 1
    board[n + 1][i] = 1
for i in range(len(apple)):
    board[apple[i][0]][apple[i][1]] = 2
snake = [[1, 1]]
board[1][1] = 1
direction = 'R'
head = 0
tail = 0
time = 0
judge = True

while judge:
    for i in range(l):
        while time < change[i][0]:
            time += 1
            if direction == 'R':
                if board[snake[head][0]][snake[head][1] + 1] == 1:
                    judge = False
                    break
                else:
                    snake.append([snake[head][0], snake[head][1] + 1])
                    if board[snake[head][0]][snake[head][1] + 1] == 0:
                        board[snake[tail][0]][snake[tail][1]] = 0
                        tail += 1
                    board[snake[head][0]][snake[head][1] + 1] = 1
                head += 1
            elif direction == 'U':
                if board[snake[head][0] - 1][snake[head][1]] == 1:
                    judge = False
                    break
                else:
                    snake.append([snake[head][0] - 1, snake[head][1]])
                    if board[snake[head][0] - 1][snake[head][1]] == 0:
                        board[snake[tail][0]][snake[tail][1]] = 0
                        tail += 1
                    board[snake[head][0] - 1][snake[head][1]] = 1
                head += 1
            elif direction == 'B':
                if board[snake[head][0] + 1][snake[head][1]] == 1:
                    judge = False
                    break
                else:
                    snake.append([snake[head][0] + 1, snake[head][1]])
                    if board[snake[head][0] + 1][snake[head][1]] == 0:
                        board[snake[tail][0]][snake[tail][1]] = 0
                        tail += 1
                    board[snake[head][0] + 1][snake[head][1]] = 1
                head += 1
            elif direction == 'L':
                if board[snake[head][0]][snake[head][1] - 1] == 1:
                    judge = False
                    break
                else:
                    snake.append([snake[head][0], snake[head][1] - 1])
                    if board[snake[head][0]][snake[head][1] - 1] == 0:
                        board[snake[tail][0]][snake[tail][1]] = 0
                        tail += 1
                    board[snake[head][0]][snake[head][1] - 1] = 1
                head += 1
        if not judge:
            break
        if change[i][1] == 'D':
            if direction == 'R':
                direction = 'B'
            elif direction == 'U':
                direction = 'R'
            elif direction == 'B':
                direction = 'L'
            elif direction == 'L':
                direction = 'U'
        elif change[i][1] == 'L':
            if direction == 'R':
                direction = 'U'
            elif direction == 'U':
                direction = 'L'
            elif direction == 'B':
                direction = 'R'
            elif direction == 'L':
                direction = 'B'
    while judge:
        time += 1
        if direction == 'R':
            if board[snake[head][0]][snake[head][1] + 1] == 1:
                judge = False
                break
            else:
                snake.append([snake[head][0], snake[head][1] + 1])
                if board[snake[head][0]][snake[head][1] + 1] == 0:
                    board[snake[tail][0]][snake[tail][1]] = 0
                    tail += 1
                board[snake[head][0]][snake[head][1] + 1] = 1
            head += 1
        elif direction == 'U':
            if board[snake[head][0] - 1][snake[head][1]] == 1:
                judge = False
                break
            else:
                snake.append([snake[head][0] - 1, snake[head][1]])
                if board[snake[head][0] - 1][snake[head][1]] == 0:
                    board[snake[tail][0]][snake[tail][1]] = 0
                    tail += 1
                board[snake[head][0] - 1][snake[head][1] + 1] = 1
            head += 1
        elif direction == 'B':
            if board[snake[head][0] + 1][snake[head][1]] == 1:
                judge = False
                break
            else:
                snake.append([snake[head][0] + 1, snake[head][1]])
                if board[snake[head][0] + 1][snake[head][1]] == 0:
                    board[snake[tail][0]][snake[tail][1]] = 0
                    tail += 1
                board[snake[head][0] + 1][snake[head][1]] = 1
            head += 1
        elif direction == 'L':
            if board[snake[head][0]][snake[head][1] - 1] == 1:
                judge = False
                break
            else:
                snake.append([snake[head][0], snake[head][1] - 1])
                if board[snake[head][0]][snake[head][1] - 1] == 0:
                    board[snake[tail][0]][snake[tail][1]] = 0
                    tail += 1
                board[snake[head][0]][snake[head][1] - 1] = 1
            head += 1
print(time)

# 뱀
from collections import deque
import sys

def solution(N, K, apples, L, turns):
    board = [[0 for _ in range(N+2)] for _ in range(N+2)]
    init(board, apples)

    dir = [(-1,0), (0,1), (1,0), (0,-1)]
    n = 1

    snake = deque()
    snake.append([1,1])

    turns = deque(turns)
    nextTurn = turns.popleft()

    time = 0
    flag = True

    while flag:
        time += 1
        flag = move(board, snake, dir[n])
        if time == nextTurn[0]:
            n = (n + nextTurn[1]) % 4
            if turns:
                nextTurn = turns.popleft()
                
        print("time=", time)
        printBoard(board, snake)
        print(snake)

    return time
    
def init(board, apples):
    n = len(board[0])
    for i in range(n):
        for j in range(n):
            if i == 0 or i == n-1 or j == 0 or j == n-1:
                board[i][j] = 1
    
    for r, c in apples:
        board[r][c] = 2
    
    board[1][1] = 1

def move(board, snake : deque, dir):
    nextPos = [snake[0][0] + dir[0], snake[0][1] + dir[1]]
    if board[nextPos[0]][nextPos[1]] == 0:
        if len(snake) == 1:
            board[snake[0][0]][snake[0][1]] = 0
            snake[0] = nextPos
            board[nextPos[0]][nextPos[1]] = 1
        else:
            snake.appendleft(nextPos)
            board[nextPos[0]][nextPos[1]] = 1
            tail = snake.pop()
            board[tail[0]][tail[1]] = 0
    elif board[nextPos[0]][nextPos[1]] == 2:
        board[nextPos[0]][nextPos[1]] = 1
        snake.appendleft(nextPos)
    elif board[nextPos[0]][nextPos[1]] == 1:
        return False
    return True

def printBoard(board, snake):
    n = len(board[0])
    for i in range(n):
        for j in range(n):
            print(board[i][j], end=" ")
        print()
    print()
    

N = int(input())
K = int(input())
apples=[]
for _ in range(K):
    r, c = map(int, sys.stdin.readline().split())
    apples.append((r,c))

L = int(input())
turns=[]
for _ in range(L):
    s, d = sys.stdin.readline().split()
    turn = (int(s), 1) if d == 'D' else (int(s), -1)
    turns.append(turn)

print(solution(N, K, apples, L, turns))

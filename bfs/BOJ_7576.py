'''
#틀린 
from collections import deque


def bfs():
    while queue:
        x, y = queue.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0 <= x < col and 0 <= y < row and box[i][j] == 0:   ## 조건 틀림 및 인덱스 번호를 잘못 붙임으로 메모리 초과.
                box[nx][ny] = box[x][y] + 1
                queue.append((x, y))  ## 큐에 이전 상태를 넣어 구현이 잘못됨. 문제 틀림.

if __name__ == "__main__":

    col, row = map(int, input().split())
    box = [list(map(int, input().split())) for _ in range(row)]
    queue = deque()
    dx = [1, -1, 0, 0]
    dy = [0, 0, -1, 1]
    
    for i in range(row):
        for j in range(col):
            if box[i][j] == 1:
                queue.append((i, j))

bfs()
isTrue = False
result = -999999
for i in box:
    for j in i:
        if j == 0:
            isTrue = True
        result = max(result, j)
if isTrue == True:
    print(-1)
elif result == -1:
    print(0)
else:
    print(result-1)
'''

from collections import deque


def bfs():
    while queue:
        x, y = queue.popleft()
        for k in range(4):
            nx = x + dx[k]
            ny = y + dy[k]
            if 0 <= nx < row and 0 <= ny < col and box[nx][ny] == 0:
                box[nx][ny] = box[x][y] + 1
                queue.append((nx, ny))


if __name__ == "__main__":

    col, row = map(int, input().split())
    box = [list(map(int, input().split())) for _ in range(row)]
    queue = deque()
    dx = [1, -1, 0, 0]
    dy = [0, 0, -1, 1]
    
    for i in range(row):
        for j in range(col):
            if box[i][j] == 1:
                queue.append((i, j))

bfs()
isTrue = False
result = -2
for i in box:
    for j in i:
        if j == 0:
            isTrue = True
        result = max(result, j)
if isTrue == True:
    print(-1)
elif result == -1:
    print(0)
else:
    print(result-1)

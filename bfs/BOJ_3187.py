#양치기 꿍
from collections import deque

def bfs(x, y):
    
    wolf_cnt = 0
    sheep_cnt = 0
    matirx_visited[x][y] = 1
    queue = deque()
    queue.append((x, y))

    while queue:
        x_p, y_p = queue.popleft()
        if matrix[x_p][y_p] == "v":
            wolf_cnt += 1
        elif matrix[x_p][y_p] == "k":
            sheep_cnt += 1
        for i in range(4):
            nx = x_p + dx[i]
            ny = y_p + dy[i]
            if 0 <= nx < row and 0 <= ny < col and matirx_visited[nx][ny] == 0 and matrix[nx][ny] != "#":
                queue.append((nx, ny))
                matirx_visited[nx][ny] = 1
    if wolf_cnt < sheep_cnt:
        wolf_cnt = 0
    elif wolf_cnt >= sheep_cnt:
        sheep_cnt = 0
    
    return wolf_cnt, sheep_cnt


if __name__ == "__main__":
    row, col = map(int, input().split())
    matrix = []
    matirx_visited = [[0]*col for _ in range(row)]
    for i in range(row):
        n = list(input())
        matrix.append(n)

    dx = [1, -1, 0, 0]
    dy = [0, 0, -1, 1]
    res_s = res_w = 0
    for i in range(row):
        for j in range(col):
            if matrix[i][j] != "#" and matirx_visited[i][j] == 0:
                w, s = bfs(i, j)
                res_w += w; res_s += s
print(res_s, res_w)

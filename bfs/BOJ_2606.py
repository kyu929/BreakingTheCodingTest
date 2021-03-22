from collections import deque


def bfs(graph, visited, start):
    count = 0
    queue = deque()
    queue.append(1)
    visited[1] = 1
    while queue:
        v = queue.popleft()
        for i in com[v]:
            if visited[i] == 0:
                queue.append(i)
                visited[i] = 1
                count += 1
    return count


if __name__ == "__main__":

    n = int(input())
    k = int(input())

    com = [[] for _ in range(1+n)]
    visited = [0] * (1 + n)

    for i in range(k):
        a, b = map(int, input().split())
        com[a].append(b)
        com[b].append(a)

    print(bfs(com, visited, 1))

n, m = map(int, input().split())
a = [list(map(int, input().split())) for _ in range(n)]

# Please write your code here.
from collections import deque

dr = [-1, +1, +0, +0]
dc = [+0, +0, -1, +1]

visited = [[False] * m for _ in range(n)]
distance = [[-1] * m for _ in range(n)]

visited[0][0] = True
distance[0][0] = 0

stack = deque([(0, 0)])

while stack:
    x, y = stack.popleft()

    for di, dj in zip(dr, dc):
        next_x, next_y = x + di, y + dj
        if 0 <= next_x < n and 0 <= next_y < m and \
        a[next_x][next_y] and (not visited[next_x][next_y]):
            visited[next_x][next_y] = True
            distance[next_x][next_y] = distance[x][y] + 1
            stack.append((next_x, next_y))

print(distance[n-1][m-1])

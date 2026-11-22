n, k = map(int, input().split())
grid = [list(map(int, input().split())) for _ in range(n)]
points = [tuple(map(int, input().split())) for _ in range(k)]

# Please write your code here.
from collections import deque

dr = [-1, +0, +1, +0]
dc = [+0, +1, +0, -1]

visited = [[False] * n for _ in range(n)]
for sp in points:
    ri, ci = sp
    ri -= 1
    ci -= 1
    
    if visited[ri][ci] == True:
        continue
    
    visited[ri][ci] = True
    que = deque([[ri, ci]])
    while que:
        r, c = que.popleft()

        for di, dj in zip(dr, dc):
            next_r = r + di
            next_c = c + dj

            if 0 <= next_r < n and 0 <= next_c < n and grid[next_r][next_c] == 0 and not visited[next_r][next_c]:
                visited[next_r][next_c] = True
                que.append([next_r, next_c])

print(sum(map(sum, visited)))

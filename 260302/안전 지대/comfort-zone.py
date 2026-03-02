n, m = map(int, input().split())
grid = [list(map(int, input().split())) for _ in range(n)]

# Please write your code here.
dr = [-1, +1, +0, +0]
dc = [+0, +0, -1, +1]


safe = []

def dfs(x, y):
    for di, dj in zip(dr, dc):
        next_i, next_j = x + di, y + dj
        if 0 <= next_i < n and 0 <= next_j < m and \
        grid[next_i][next_j] and (not visited[next_i][next_j]):
            visited[next_i][next_j] = True
            dfs(next_i, next_j)

for k in range(1, max(map(max, grid))):
    # 침수
    for i in range(n):
        for j in range(m):
            if grid[i][j] <= k:
                grid[i][j] = 0

    visited = [[False] * m for _ in range(n)]
    region = 0
    for i in range(n):
        for j in range(m):
            if grid[i][j] and (not visited[i][j]):
                visited[i][j] = True
                dfs(i, j)
                region += 1
    safe.append((k, region))

if safe:
    safe.sort(key=lambda r: r[1], reverse=True)
    print(safe[0][0], safe[0][1])
else:
    print(1, 0)

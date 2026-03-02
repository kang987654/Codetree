n, m = map(int, input().split())
grid = [list(map(int, input().split())) for _ in range(n)]

# Please write your code here.
dr = [+1, +0]
dc = [+0, +1]

visited = [[False] * m for _ in range(n)]
visited[0][0] = True

def dfs(x, y):
    for di, dj in zip(dr, dc):
        next_i, next_j = x + di, y + dj
        if 0 <= next_i < n and 0 <= next_j < m and \
        grid[next_i][next_j] and (not visited[next_i][next_j]):
            visited[next_i][next_j] = True
            dfs(next_i, next_j)

dfs(0, 0)
print(int(visited[n-1][m-1]))

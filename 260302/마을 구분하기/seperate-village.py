n = int(input())
grid = [list(map(int, input().split())) for _ in range(n)]

# Please write your code here.
dr = [-1, +1, +0, +0]
dc = [+0, +0, -1, +1]

visited = [[False] * n for _ in range(n)]
village = []
p = 0

def dfs(x, y):
    global p

    for di, dj in zip(dr, dc):
        next_i, next_j = x + di, y + dj
        if 0 <= next_i < n and 0 <= next_j < n and \
        grid[next_i][next_j] and (not visited[next_i][next_j]):
            visited[next_i][next_j] = True
            p += 1
            dfs(next_i, next_j)

for i in range(n):
    for j in range(n):
        if grid[i][j] and (not visited[i][j]):
            visited[i][j] = True
            p = 1
            dfs(i, j)
            village.append(p)

print(len(village))
for n in sorted(village):
    print(n)

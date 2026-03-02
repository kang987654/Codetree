n = int(input())
grid = [list(map(int, input().split())) for _ in range(n)]

# Please write your code here.
dr = [-1, +1, +0, +0]
dc = [+0, +0, -1, +1]

pung = []
lens = []
stack = []

def dfs(x, y):
    global len_t

    stack.append((x, y))

    while stack:
        now_x, now_y = stack.pop()

        for di, dj in zip(dr, dc):
            next_i, next_j = now_x + di, now_y + dj
            if 0 <= next_i < n and 0 <= next_j < n and \
            grid[next_i][next_j] == target and (not visited[next_i][next_j]):
                visited[next_i][next_j] = True
                len_t += 1
                stack.append((next_i, next_j))


visited = [[False] * n for _ in range(n)]
for i in range(n):
    for j in range(n):
        if (not visited[i][j]):
            visited[i][j] = True

            target = grid[i][j]
            len_t = 1
            dfs(i, j)
            if len_t >= 4:
                pung.append(target)
            lens.append(len_t)

print(len(pung), max(lens))

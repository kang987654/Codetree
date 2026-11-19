n = int(input())
grid = [list(map(int, input().split())) for _ in range(n)]

# Please write your code here.
def dfs(x, _list):
    global min_max

    if x == n:
        min_max = max(min(_list), min_max)
        return

    for i in range(n):
        if not visited[i]:
            visited[i] = True
            dfs(x+1, _list + [grid[i][x]])
            visited[i] = False

min_max = 0
visited = [False] * n
dfs(0, [])

print(min_max)
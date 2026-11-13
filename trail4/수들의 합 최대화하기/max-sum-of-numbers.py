n = int(input())
grid = [list(map(int, input().split())) for _ in range(n)]

# Please write your code here.
def dfs(x, _sum):
    global max_sum

    if x == n:
        max_sum = max(_sum, max_sum)
        return

    for i in range(n):
        if not visited[i]:
            visited[i] = True
            dfs(x+1, _sum + grid[i][x])
            visited[i] = False

max_sum = 0
visited = [False] * n
dfs(0, 0)

print(max_sum)

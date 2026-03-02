n, m = map(int, input().split())
edges = [tuple(map(int, input().split())) for _ in range(m)]

# Please write your code here.
cnt = 0
visited = [False] * 1001
visited[1] = True

def dfs(v):
    global cnt

    for a, b in edges:
        if a == v and (not visited[b]):
            cnt += 1
            visited[b] = True
            dfs(b)
        if b == v and (not visited[a]):
            cnt += 1
            visited[a] = True
            dfs(a)

dfs(1)
print(cnt)

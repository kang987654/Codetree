n, m = map(int, input().split())

# Please write your code here.
dr = [+0, +1, +0, -1]
dc = [+1, +0, -1, +0]
alpha = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
arr = [[0] * m for _ in range(n)]

d = 0
r, c = 0, 0
for i in range(n*m):
    arr[r][c] = alpha[i % len(alpha)]
    if not ((0 <= r+dr[d] < n and 0 <= c+dc[d] < m) and arr[r+dr[d]][c+dc[d]] == 0):
        d = (d+1) % 4
    r += dr[d]
    c += dc[d]

for a in arr:
    print(*a)

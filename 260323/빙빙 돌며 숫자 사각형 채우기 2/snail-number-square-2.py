n, m = map(int, input().split())

# Please write your code here.
dr = [+0, +1, +0, -1]
dc = [+1, +0, -1, +0]

arr = [[0] * m for _ in range(n)]

d = 1
r, c = 0, 0
for i in range(1, n*m + 1):
    arr[r][c] = i
    if not ((0 <= r+dr[d] < n and 0 <= c+dc[d] < m) and arr[r+dr[d]][c+dc[d]] == 0):
        d = (d+4-1) % 4
    r += dr[d]
    c += dc[d]

for a in arr:
    print(*a)

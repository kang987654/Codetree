n = int(input())
grid = [[0] * n for _ in range(n)]

# Please write your code here.
dr = [+0, +1, +0, -1]
dc = [+1, +0, -1, +0]

d = 0
r, c = n // 2, n // 2

i = 1
_len = 1
while i <= n*n:
    for _ in range(_len):
        grid[r][c] = i
        i += 1
        r += dr[d]
        c += dc[d]
    d = (d+4 - 1) % 4

    if i >= n*n:
        break

    for _ in range(_len):
        grid[r][c] = i
        i += 1
        r += dr[d]
        c += dc[d]
    d = (d+4 - 1) % 4

    _len += 1

for row in grid:
    print(*row)

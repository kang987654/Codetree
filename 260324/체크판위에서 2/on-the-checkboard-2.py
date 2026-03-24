R, C = map(int, input().split())
grid = [list(input().split()) for _ in range(R)]

# Please write your code here.
start = grid[0][0]

first = []
for i in range(1, R-1):
    for j in range(1, C-1):
        if grid[i][j] != start:
            first.append((i, j))

cnt = 0
while first:
    r, c = first.pop()

    for i in range(r+1, R-1):
        for j in range(c+1, C-1):
            if grid[i][j] == start:
                cnt += 1

print(cnt)

n, t = map(int, input().split())
r, c, d = input().split()
r, c = int(r), int(c)

# Please write your code here.
dr = [-1, +1, +0, +0]
dc = [+0, +0, -1, +1]

if d == 'U':
    d = 0
if d == 'D':
    d = 1
if d == 'L':
    d = 2
if d == 'R':
    d = 3

s = 1
for _ in range(t+1):
    next_r, next_c = r + s*dr[d], c + s*dc[d]
    if not (0 <= next_r < n and 0 <= next_c < n):
        s *= -1
        next_r, next_c = r + s*dr[d], c + s*dc[d]
    r, c = next_r, next_c

print(r, c)

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

# 수치 조정
r, c = r-1, c-1
s = 1   # sign
for _ in range(t):
    next_r, next_c = r + s*dr[d], c + s*dc[d]
    if 0 <= next_r < n and 0 <= next_c < n:
        r, c = next_r, next_c
    else:
        s *= -1

print(r+1, c+1)

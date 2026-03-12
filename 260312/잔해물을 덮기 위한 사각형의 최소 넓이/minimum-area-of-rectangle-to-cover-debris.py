x1, y1, x2, y2 = [0] * 2, [0] * 2, [0] * 2, [0] * 2
x1[0], y1[0], x2[0], y2[0] = map(int, input().split())
x1[1], y1[1], x2[1], y2[1] = map(int, input().split())

# Please write your code here.
offset = 1000

new_plane = [[0] * 2000 for _ in range(2000)]
v = 1
for r1, c1, r2, c2 in zip(x1, y1, x2, y2):
    for r in range(r1 + offset, r2 + offset):
        for c in range(c1 + offset, c2 + offset):
            new_plane[r][c] = v
    v -= 1

a1, b1, a2, b2 = 0, 0, 0, 0
got_first = False
for i in range(2000):
    for j in range(2000):
        if new_plane[i][j] == 1:
            a2, b2 = i, j
            if not got_first:
                a1, b1 = i, j
                got_first = True

print((a2+1 - a1) * (b2+1 - b1))

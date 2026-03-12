n = int(input())
x1, y1, x2, y2 = [], [], [], []
for _ in range(n):
    a, b, c, d = map(int, input().split())
    x1.append(a)
    y1.append(b)
    x2.append(c)
    y2.append(d)

# Please write your code here.
offset = 100

new_plane = [[0] * 200 for _ in range(200)]
v = 0
for r1, c1, r2, c2 in zip(x1, y1, x2, y2):
    for r in range(r1 + offset, r2 + offset):
        for c in range(c1 + offset, c2 + offset):
            new_plane[r][c] = v
    v = (v+1) % 2

print(sum(map(sum, new_plane)))

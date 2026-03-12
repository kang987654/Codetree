x1 = [0] * 3
y1 = [0] * 3
x2 = [0] * 3
y2 = [0] * 3

x1[0], y1[0], x2[0], y2[0] = map(int, input().split())
x1[1], y1[1], x2[1], y2[1] = map(int, input().split())
x1[2], y1[2], x2[2], y2[2] = map(int, input().split())

# Please write your code here.
offset = 1000

new_plane = [[0] * 2000 for _ in range(2000)]
idx = 0
for r1, c1, r2, c2 in zip(x1, y1, x2, y2):
    if idx == 0 or idx == 1:
        for r in range(r1 + offset, r2 + offset):
            for c in range(c1 + offset, c2 + offset):
                new_plane[r][c] = 1
        idx += 1
    else:
        for r in range(r1 + offset, r2 + offset):
            for c in range(c1 + offset, c2 + offset):
                new_plane[r][c] = 0


print(sum(map(sum, new_plane)))

n = int(input())
points = [tuple(map(int, input().split())) for _ in range(n)]
x, y = zip(*points)
x, y = list(x), list(y)

# Please write your code here.
offset = 100

new_plane = [[0] * 200 for _ in range(200)]
for r1, c1 in zip(x, y):
    for r in range(r1 + offset, r1+8 + offset):
        for c in range(c1 + offset, c1+8 + offset):
            new_plane[r][c] = 1

print(sum(map(sum, new_plane)))

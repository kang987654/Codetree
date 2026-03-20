dirs = input()

# Please write your code here.
d = [(0, +1), (+1, 0), (0, -1), (-1, 0)]

x, y = 0, 0
see = 0
for dir in dirs:
    if dir == 'L':
        see = (see+4 - 1) % 4
    if dir == 'R':
        see = (see + 1) % 4
    if dir == 'F':
        dx, dy = d[see]
        x += dx
        y += dy

print(x, y)

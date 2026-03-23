commands = input()

# Please write your code here.
dir = [
    (+0, +1),
    (+1, +0),
    (+0, -1),
    (-1, +0)
]

x, y = 0, 0
d = 0
answer = -1
t = 0
for command in commands:
    t += 1
    if command == 'F':
        dx, dy = dir[d]
        x += dx
        y += dy
    if command == 'R':
        d = (d+1) % 4
    if command == 'L':
        d = (d+4-1) % 4

    if x == 0 and y == 0:
        answer = t
        break

print(answer)

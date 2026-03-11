n = int(input())
commands = [tuple(input().split()) for _ in range(n)]
x = []
dir = []
for num, direction in commands:
    x.append(int(num))
    dir.append(direction)

# Please write your code here.
state = [0] * 200001
color = ['N'] * 200001
now = 100000
for i in range(n):
    if dir[i] == 'L':
        now += 1
        for _ in range(x[i]):
            now -= 1
            
            color[now] = 'W'
    else:
        now -= 1
        for _ in range(x[i]):
            now += 1
            
            color[now] = 'B'

w, b = 0, 0
for c in color:
    if c == 'W':
        w += 1
    if c == 'B':
        b += 1

print(w, b)

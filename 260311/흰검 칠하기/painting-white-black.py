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
            
            state[now] += 100
            color[now] = 'W'
    else:
        now -= 1
        for _ in range(x[i]):
            now += 1
            
            state[now] += 1
            color[now] = 'B'

w, b, g = 0, 0, 0
for i, s in enumerate(state):
    if s // 100 >= 2 and s % 100 >= 2:
        g += 1
    elif color[i] == 'W':
        w += 1
    elif color[i] == 'B':
        b += 1

print(w, b, g)

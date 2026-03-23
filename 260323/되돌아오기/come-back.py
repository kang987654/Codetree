N = int(input())
moves = [tuple(input().split()) for _ in range(N)]
dir = [move[0] for move in moves]
dist = [int(move[1]) for move in moves]

# Please write your code here.
head = {
    'W': (-1, +0),
    'S': (+0, -1),
    'N': (+0, +1),
    'E': (+1, +0)
}

time = 0
answer = -1
x, y = 0, 0
for d, t in zip(dir, dist):
    dx, dy = head[d]
    for i in range(1, t+1):
        time += 1
        x += dx
        y += dy
    
        if x == 0 and y == 0:
            answer = time
    if answer != -1:
        break

print(answer)

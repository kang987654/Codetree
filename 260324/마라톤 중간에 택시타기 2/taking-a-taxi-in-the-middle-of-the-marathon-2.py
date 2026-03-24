n = int(input())
points = [tuple(map(int, input().split())) for _ in range(n)]
x = [p[0] for p in points]
y = [p[1] for p in points]

# Please write your code here.
dist = []
for skip in range(1, n-1):
    prev_x, prev_y = x[0], y[0]
    d = 0
    for i in range(1, n):
        if i == skip:
            continue
        
        now_x, now_y = x[i], y[i]
        d += abs(prev_x - now_x) + abs(prev_y - now_y)
        prev_x, prev_y = now_x, now_y
    dist.append(d)

print(min(dist))

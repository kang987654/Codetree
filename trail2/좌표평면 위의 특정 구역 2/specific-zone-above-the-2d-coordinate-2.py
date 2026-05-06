n = int(input())
points = [tuple(map(int, input().split())) for _ in range(n)]
x = [p[0] for p in points]
y = [p[1] for p in points]

# Please write your code here.
from collections import deque

x = deque(x)
y = deque(y)

min_sq = float('inf')
for _ in range(n):
    pop_x, pop_y = x.popleft(), y.popleft()
    min_sq = min(min_sq, abs(max(x)-min(x)) * abs(max(y)- min(y)))
    x.append(pop_x)
    y.append(pop_y)

print(min_sq)

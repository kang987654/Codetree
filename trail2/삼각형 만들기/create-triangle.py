n = int(input())
points = [tuple(map(int, input().split())) for _ in range(n)]
x = [p[0] for p in points]
y = [p[1] for p in points]

# Please write your code here.
from itertools import combinations

max_tri = 0
for i, j, k in combinations(range(n), 3):
    # x축에 평행
    if not (x[i] == x[j] or x[j] == x[k] or x[i] == x[k]):
        continue
    # y축에 평행
    if not (y[i] == y[j] or y[j] == y[k] or y[i] == y[k]):
        continue
    
    now_tri = (max(x[i], x[j], x[k]) - min(x[i], x[j], x[k])) * (max(y[i], y[j], y[k]) - min(y[i], y[j], y[k]))
    max_tri = max(max_tri, now_tri)

print(max_tri)
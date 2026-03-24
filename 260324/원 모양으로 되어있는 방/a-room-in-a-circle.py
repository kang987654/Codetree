n = int(input())
a = [int(input()) for _ in range(n)]

# Please write your code here.
from collections import deque

a = deque(a)
dist = []
for _ in range(n):
    d = 0
    for i in range(n):
        d += a[i] * i
    dist.append(d)
    a.append(a.popleft())

print(min(dist))

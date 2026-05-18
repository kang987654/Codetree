n = int(input())
l = []
r = []
for _ in range(n):
    left, right = map(int, input().split())
    l.append(left)
    r.append(right)

# Please write your code here.
from itertools import combinations

count = 0
origin = [0] * 101
for i in range(n):
    for line in range(l[i], r[i]+1):
        origin[line] += 1

for i, j, k in combinations(range(n), 3):
    copy = origin[:]
    for line in range(l[i], r[i]+1):
        copy[line] -= 1
    
    for line in range(l[j], r[j]+1):
        copy[line] -= 1
        
    for line in range(l[k], r[k]+1):
        copy[line] -= 1
    
    if max(copy) <= 1:
        count += 1

print(count)
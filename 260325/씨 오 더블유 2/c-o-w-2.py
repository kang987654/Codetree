n = int(input())
S = input()

# Please write your code here.
from itertools import combinations

c = []
o = []
w = []
for i, s in enumerate(S):
    if s == 'C':
        c.append(i)
    if s == 'O':
        o.append(i)
    if s == 'W':
        w.append(i)

cnt = 0
for i, j, k in combinations(c+o+w, 3):
    if i in c and j in o and k in w and i < j < k:
        cnt += 1

print(cnt)

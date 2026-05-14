k, n = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(k)]

# Please write your code here.
from itertools import permutations

pair_dict = {}
for a, b in permutations(range(1, n+1), 2):
    pair_dict[(a, b)] = 0

for a in arr:
    for i in range(n):
        for j in range(i+1, n):
            pair_dict[(a[i], a[j])] += 1

pair_num = 0
for p, v in pair_dict.items():
    if v == k:
        pair_num += 1

print(pair_num)

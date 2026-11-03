n, m = map(int, input().split())
A = list(map(int, input().split()))

# Please write your code here.
from itertools import combinations

max_val = 0
for comb in combinations(A, m):
    val = 0
    for c in comb:
        val ^= c
    max_val = max(max_val, val)

print(max_val)

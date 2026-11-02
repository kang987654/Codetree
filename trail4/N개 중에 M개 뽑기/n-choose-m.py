N, M = map(int, input().split())

# Please write your code here.
from itertools import combinations

for comb in combinations(range(1, N+1), M):
    print(*comb)
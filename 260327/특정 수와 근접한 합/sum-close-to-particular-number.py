N, S = map(int, input().split())
arr = list(map(int, input().split()))

# Please write your code here.
from itertools import combinations

answer = float('inf')
total = sum(arr)
for n, m in combinations(arr, 2):
    T = total - (n+m)
    answer = min(abs(T-S), answer)

print(answer)

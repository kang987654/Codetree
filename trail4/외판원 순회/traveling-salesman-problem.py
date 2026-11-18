n = int(input())
A = [list(map(int, input().split())) for _ in range(n)]

# Please write your code here.
from itertools import permutations

min_cost = float('inf')
for per in permutations(range(1, n), n-1):
    this_cost = 0
    i = 0
    for j in list(per) + [0]:
        if A[i][j] == 0:
            this_cost = float('inf')
            break
        this_cost += A[i][j]
        i = j
    min_cost = min(this_cost, min_cost)

print(min_cost)
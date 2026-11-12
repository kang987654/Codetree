n = int(input())

# Please write your code here.
from itertools import permutations

for per in permutations(range(n, 0, -1), n):
    print(*per)

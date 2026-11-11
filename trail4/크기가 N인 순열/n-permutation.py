n = int(input())

# Please write your code here.
from itertools import permutations

for p in permutations(range(1, n+1), n):
    print(*p)
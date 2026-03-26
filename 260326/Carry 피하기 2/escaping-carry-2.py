n = int(input())
arr = [int(input()) for _ in range(n)]

# Please write your code here.
from itertools import combinations

def avoid_carry(a, b, c):
    while a or b or c:
        _a = int(a.pop()) if a else 0
        _b = int(b.pop()) if b else 0
        _c = int(c.pop()) if c else 0
        if sum([_a, _b, _c]) >= 10:
            return False
    return True


max_sum = -1
for i, j, k in combinations(arr, 3):
    if avoid_carry(list(str(i)), list(str(j)), list(str(k))):
        max_sum = max(max_sum, sum([i, j, k]))

print(max_sum)

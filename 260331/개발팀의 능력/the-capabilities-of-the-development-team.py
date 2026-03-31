arr = list(map(int, input().split()))

# Please write your code here.
from itertools import combinations, permutations

answer = float('inf')

origin = set(arr)
for a, b in combinations(arr, 2):
    for c, d, e in permutations(list(origin-set([a,b])), 3):
        s1, s2, s3 = a+b, c+d, e
        if s1 != s2 and s1 != s3 and s2 != s3:
            answer = min(max(s1, s2, s3) - min(s1, s2, s3), answer)

print(answer if answer != float('inf') else -1)

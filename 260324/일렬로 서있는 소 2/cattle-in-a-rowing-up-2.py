N = int(input())
A = list(map(int, input().split()))

# Please write your code here.
from itertools import combinations

cnt = 0
cow = list(range(N))
for i, j, k in combinations(cow, 3):
    if i < j < k and A[i] < A[j] < A[k]:
        cnt += 1

print(cnt)

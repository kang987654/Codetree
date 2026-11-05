n = int(input())
num = list(map(int, input().split()))

# Please write your code here.
from itertools import combinations

index_list = list(range(2*n))
min_sum = float('inf')
for pair1 in combinations(index_list, n):
    pair1_num, pair2_num = [], []
    for p in pair1:
        pair1_num.append(num[p])
    pair2 = list(set(index_list) - set(pair1))
    for p in pair2:
        pair2_num.append(num[p])
    min_sum = min(min_sum, abs(sum(pair1_num) - sum(pair2_num)))

print(min_sum)

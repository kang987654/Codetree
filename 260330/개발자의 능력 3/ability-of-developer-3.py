abilities = list(map(int, input().split()))

# Please write your code here.
from itertools import combinations
sum_abil = sum(abilities)

min_abil = float('inf')
for i, j, k in combinations(abilities, 3):
    team1 = i+j+k
    team2 = sum_abil - team1

    diff = abs(team2-team1)
    min_abil = min(diff, min_abil)

print(min_abil)

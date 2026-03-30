n = int(input())
people = [tuple(input().split()) for _ in range(n)]
pos = [int(p[0]) for p in people]
alpha = [p[1] for p in people]

# Please write your code here.
# 최대 100 개 이므로 g 1 h 100 이면
# 101로 나누어 쌍이 맞는지 확인
alpha = [1 if a == 'G' else 100 for a in alpha]
people = sorted(zip(pos, alpha), key=lambda pa: pa[0])

s_alpha = [p[1] for p in people]
def max_pair():
    for size in range(n, 1, -1):
        for i in range(n+1 - size):
            if sum(s_alpha[i:i+size]) % 101 == 0:
                l = i
                r = i+size-1

                return people[r][0] - people[l][0]
    return 0

print(max_pair())

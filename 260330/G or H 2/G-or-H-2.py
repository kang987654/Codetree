n = int(input())
people = [tuple(input().split()) for _ in range(n)]
pos = [int(p[0]) for p in people]
alpha = [p[1] for p in people]

# Please write your code here.
alpha = [1 if a == 'G' else 100 for a in alpha]
people = sorted(zip(pos, alpha), key=lambda pa: pa[0])

s_alpha = [p[1] for p in people]
def max_pair():
    for size in range(n, 1, -1):
        for i in range(n+1 - size):
            # G 로만 or H 로만 or 정확히 같은 개수
            if 1 < sum(s_alpha[i:i+size]) < 100 or \
            (100 < sum(s_alpha[i:i+size]) and sum(s_alpha[i:i+size]) % 100 == 0) or \
            sum(s_alpha[i:i+size]) % 101 == 0:
                l = i
                r = i+size-1

                return people[r][0] - people[l][0]
    return 0

print(max_pair())

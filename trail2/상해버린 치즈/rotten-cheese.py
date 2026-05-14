N, M, D, S = map(int, input().split())

p, m, t = [], [], []
for _ in range(D):
    person, milk, time = map(int, input().split())
    p.append(person)
    m.append(milk)
    t.append(time)

sick_p, sick_t = [], []
for _ in range(S):
    person, time = map(int, input().split())
    sick_p.append(person)
    sick_t.append(time)

# Please write your code here.
# 상한 치즈 찾기
gone_cheeze_count = [0] * (M+1)
for i in range(S):
    person, time = sick_p[i], sick_t[i]
    for j in range(D):
        per, che, tim = p[j], m[j], t[j]
        if per == person and tim < time:
            gone_cheeze_count[che] += 1
gone_cheeze = []
for i in range(M+1):
    if gone_cheeze_count[i] == max(gone_cheeze_count):
        gone_cheeze.append(i)

# 필요한 c최대 약의 수 구하기
max_pill = 0
for c in gone_cheeze:
    ate_cheeze = [False] * (N+1)
    for i in range(D):
        per, che, tim = p[i], m[i], t[i]
        if che == c:
            ate_cheeze[per] = True
    max_pill = max(max_pill, sum(ate_cheeze))

print(max_pill)

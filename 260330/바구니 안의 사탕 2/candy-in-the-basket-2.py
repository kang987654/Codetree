N, K = map(int, input().split())
candy = []
pos = []

for _ in range(N):
    c, p = map(int, input().split())
    candy.append(c)
    pos.append(p)

# Please write your code here.
bucket = [0] * max(pos)
for i in range(N):
    bucket[pos[i]-1] += candy[i]

answer = 0
for i in range(K, len(bucket)-K+1):
    answer = max(sum(bucket[i-K:i+K+1]), answer)

print(answer)

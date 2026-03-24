n = int(input())
A = list(map(int, input().split()))

# Please write your code here.
dist = []
for i in range(n):
    tmp = 0
    for j in range(n):
        tmp += abs(j-i) * A[j]
    dist.append(tmp)

print(min(dist))

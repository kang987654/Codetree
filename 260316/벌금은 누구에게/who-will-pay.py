N, M, K = map(int, input().split())
student = [int(input()) for _ in range(M)]

# Please write your code here.
p = [0] * (N+1)
for s in student:
    p[s] += 1
    if p[s] >= K:
        print(s)
        break
else:
    print(-1)

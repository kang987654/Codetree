N, M = map(int, input().split())
A = list(map(int, input().split()))
B = list(map(int, input().split()))

# Please write your code here.
cnt = 0
for i in range(N-M+1):
    tmp = A[i:i+M]
    if sorted(tmp) == sorted(B):
        cnt += 1

print(cnt)

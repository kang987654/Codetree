N, M = map(int, input().split())
A = list(map(int, input().split()))
B = list(map(int, input().split()))

# Please write your code here.
cnt = 0
for i in range(N-M+1):
    tmp = set(A[i:i+M])
    if tmp == set(B):
        cnt += 1

print(cnt)

n = int(input())
A = list(map(int, input().split()))
B = list(map(int, input().split()))

# Please write your code here.
A.sort()
B.sort()

for i in range(len(A)):
    if A[i] != B[i]:
        print('No')
        break
else:
    print('Yes')
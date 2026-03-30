N = int(input())
a, b, c = map(int, input().split())

# Please write your code here.
origin = set(range(1, N+1))
A = set(range(a-2, a+3))
B = set(range(b-2, b+3))
C = set(range(c-2, c+3))

not_answer = (N - len(A & origin)) * (N - len(B & origin)) * (N - len(C & origin))
answer = N*N*N - not_answer
print(answer)

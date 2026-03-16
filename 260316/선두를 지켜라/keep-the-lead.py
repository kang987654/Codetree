n, m = map(int, input().split())

# Process A's movements
v = []
t = []
for _ in range(n):
    vi, ti = map(int, input().split())
    v.append(vi)
    t.append(ti)

# Process B's movements
v2 = []
t2 = []
for _ in range(m):
    vi, ti = map(int, input().split())
    v2.append(vi)
    t2.append(ti)

# Please write your code here.
A, B = [], []
for vi, ti in zip(v, t):
    A += [vi] * ti
for vi, ti in zip(v2, t2):
    B += [vi] * ti

a, b = 0, 0
i = 0
prev = 's'
cnt = 0
while i < sum(t):
    a += A[i]
    b += B[i]
    i += 1

    if a > b and prev != 'a':
        cnt += 1
        prev = 'a'
    if a < b and prev != 'b':
        cnt += 1
        prev = 'b'

print(cnt)
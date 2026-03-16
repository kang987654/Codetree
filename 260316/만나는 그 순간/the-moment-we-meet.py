n, m = map(int, input().split())

d = []
t = []
for _ in range(n):
    direction, time = input().split()
    d.append(direction)
    t.append(int(time))

d2 = []
t2 = []
for _ in range(m):
    direction, time = input().split()
    d2.append(direction)
    t2.append(int(time))

# Please write your code here.
A, B = [], []
for di, ti in zip(d, t):
    if di == 'R':
        A += [1] * ti
    else:
        A += [-1] * ti
for di, ti in zip(d2, t2):
    if di == 'R':
        B += [1] * ti
    else:
        B += [-1] * ti
A = A * (1000 * 1000 // len(A))
B = B * (1000 * 1000 // len(B))

a, b = 0, 0
i = 0
while i < 1000 * 1000:
    a += A[i]
    b += B[i]
    i += 1

    if a == b:
        print(i)
        break
    
if i == 1000 * 1000:
    print(-1)

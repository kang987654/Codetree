n = int(input())
x = []
dir = []
for _ in range(n):
    xi, di = input().split()
    x.append(int(xi))
    dir.append(di)

# Please write your code here.
ground = [0] * 2001
now = 1000
for i in range(n):
    if dir[i] == 'L':
        for _ in range(x[i]):
            now -= 1
            ground[now] += 1
    else:
        for _ in range(x[i]):
            ground[now] += 1
            now += 1

cnt = 0
for g in ground:
    if g >= 2:
        cnt += 1

print(cnt)

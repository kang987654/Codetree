N, B = map(int, input().split())
gifts = [list(map(int, input().split())) for _ in range(N)]
P = [gift[0] for gift in gifts]
S = [gift[1] for gift in gifts]

# Please write your code here.
max_students = 0
for i in range(N):
    gifts[i][0] //= 2
    n, b = 0, 0
    for p, s in sorted(gifts, key=lambda gift: gift[0]+gift[1]):
        b += p+s
        if b > B:
            max_students = max(max_students, n)
            break
        n += 1
    gifts[i][0] *= 2

print(max_students)
n = int(input())
points = [tuple(map(int, input().split())) for _ in range(n)]
x = [p[0] for p in points]
y = [p[1] for p in points]

# Please write your code here.
min_dis = float('inf')
for i in range(n):
    for j in range(i+1, n):
        tmp_dis = (x[i] - x[j]) ** 2 + (y[i] - y[j]) ** 2
        min_dis = min(min_dis, tmp_dis)

print(min_dis)
n = int(input())
times = [tuple(map(int, input().split())) for _ in range(n)]
a = [t[0] for t in times]
b = [t[1] for t in times]

# Please write your code here.
working_hours = 0
for i in range(n):
    table = [False] * 1000
    for j in range(n):
        if j == i:
            continue
        for k in range(a[j], b[j]):
            table[k] = True
    working_hours = max(working_hours, sum(table))

print(working_hours)
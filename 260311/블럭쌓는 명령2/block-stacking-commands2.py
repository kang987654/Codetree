n, k = map(int, input().split())
commands = [tuple(map(int, input().split())) for _ in range(k)]

# Please write your code here.
ground = [0] * 101
for s, e in commands:
    for i in range(s, e+1):
        ground[i] += 1

print(max(ground))

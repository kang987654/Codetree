n = int(input())
lines = [tuple(map(int, input().split())) for _ in range(n)]

# Please write your code here.
is_alone = [True] * n
for i in range(n):
    x1, x2 = lines[i]
    for j in range(i+1, n):
        s1, s2 = lines[j]
        if (x1 < s1 and x2 > s2) or (x1 > s1 and x2 < s2):
            is_alone[i] = False
            is_alone[j] = False

print(sum(is_alone))
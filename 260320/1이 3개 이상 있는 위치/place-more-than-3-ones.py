n = int(input())
grid = [list(map(int, input().split())) for _ in range(n)]

# Please write your code here.
d4 = [(-1, +0), (+1, +0), (+0, -1), (+0, +1)]

answer = 0
for i in range(n):
    for j in range(n):
        cnt = 0
        for di, dj in d4:
            near_i, near_j = i + di, j + dj
            if 0 <= near_i < n and 0 <= near_j < n and grid[near_i][near_j]:
                cnt += 1
        if cnt >= 3:
            answer += 1

print(answer)
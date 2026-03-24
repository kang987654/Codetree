n = int(input())
grid = [list(map(int, input().split())) for _ in range(n)]

# Please write your code here.
coin = 0
for i in range(n):
    for j in range(n-2):
        coin = max(sum(grid[i][j:j+3]), coin)

print(coin)

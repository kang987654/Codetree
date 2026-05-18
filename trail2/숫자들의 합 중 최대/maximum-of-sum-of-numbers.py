X, Y = map(int, input().split())

# Please write your code here.
max_sum = 0
for num in range(X, Y+1):
    tmp = 0
    while num > 0:
        tmp += num % 10
        num //= 10
    max_sum = max(max_sum, tmp)

print(max_sum)
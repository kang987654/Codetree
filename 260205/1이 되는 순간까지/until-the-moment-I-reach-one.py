N = int(input())

# Please write your code here.
def until_one(n):
    if n == 1:
        return 0

    if n % 2 == 0:
        n = int(n / 2)
    else:
        n = n // 3
    return until_one(n) + 1

print(until_one(N))
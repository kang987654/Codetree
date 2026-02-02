a, b = map(int, input().split())

# Please write your code here.
def is_prime(n):
    for i in range(n-1, 1, -1):
        if n % i == 0:
            return False
    return True

def is_sum_even(n):
    sum = n % 10
    while n >= 10:
        n //= 10
        sum += n % 10
    if sum % 2 == 0:
        return True
    return False

cnt = 0
for i in range(a, b+1):
    if is_prime(i) and is_sum_even(i):
        cnt += 1

print(cnt)
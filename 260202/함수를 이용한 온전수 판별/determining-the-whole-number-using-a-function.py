a, b = map(int, input().split())

# Please write your code here.
def is_perfect(n):
    if n % 2 == 0:
        return False
    if n % 10 == 5:
        return False
    if n % 3 == 0 and n % 9 != 0:
        return False
    return True

cnt = 0
for n in range(a, b+1):
    if is_perfect(n):
        cnt += 1

print(cnt)
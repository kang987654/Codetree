M, D = map(int, input().split())

# Please write your code here.
def is_valid_day(M, D):
    if M == 2 and 0 < D < 29:
        return True
    if M in [1, 3, 5, 7, 8, 10, 12] and 0 < D < 32:
        return True
    if M in [4, 6, 9, 11] and 0 < D < 31:
        return True
    return False

if is_valid_day(M, D):
    print('Yes')
else:
    print('No')
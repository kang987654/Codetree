Y, M, D = map(int, input().split())

# Please write your code here.
def is_yoon(Y):
    if (Y % 400) == 0:
        return True
    if (Y % 100) == 0:
        return False
    if (Y % 4) == 0:
        return True
    return False

def is_valid_day(Y, M, D):
    if M == 2 and (is_yoon(Y) and 0 < D < 30) or 0 < D < 29:
        return True
    if M in [1, 3, 5, 7, 8, 10, 12] and 0 < D < 32:
        return True
    if M in [4, 6, 9, 11] and 0 < D < 31:
        return True
    return False

if is_valid_day(Y, M, D):
    if 3 <= M <= 5:
        print('Spring')
    if 6 <= M <= 8:
        print('Summer')
    if 9 <= M <= 11:
        print('Fall')
    if M == 12 or M == 1 or M == 2:
        print('Winter')
else:
    print(-1)
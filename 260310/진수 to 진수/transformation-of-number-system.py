a, b = map(int, input().split())
n = input()

# Please write your code here.
def a_to_dec(_a):
    n, i = 0, 0
    for ai in _a[::-1]:
        n += int(ai) * a**i
        i += 1

    return n


def dec_to_b(n):
    _b = ''
    while n >= b:
        _b = str(n % b) + _b
        n = n // b
    
    return str(n) + _b


print(dec_to_b(a_to_dec(n)))

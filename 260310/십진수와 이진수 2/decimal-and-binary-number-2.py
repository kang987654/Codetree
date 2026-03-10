N = input()

# Please write your code here.
def bin_to_dec(_bin):
    n, i = 0, 0
    for b in _bin[::-1]:
        n += int(b) * 2**i
        i += 1

    return n


def dec_to_bin(n):
    _bin = ''
    while n >= 2:
        _bin = str(n%2) + _bin
        n = n // 2
    
    return str(n) + _bin


print(dec_to_bin(bin_to_dec(N) * 17))

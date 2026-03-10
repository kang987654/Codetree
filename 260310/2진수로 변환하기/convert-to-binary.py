n = int(input())

# Please write your code here.
_bin = ''

while n != 1:
    _bin = str(n%2) + _bin
    n = n // 2

print(str(n) + _bin)

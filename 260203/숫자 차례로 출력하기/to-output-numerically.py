n = int(input())

# Please write your code here.
def inc(n):
    if n == 0:
        return
    inc(n-1)
    print(n, end=' ')

def dec(n):
    if n == 0:
        return
    print(n, end=' ')
    dec(n-1)

inc(n)
print()
dec(n)
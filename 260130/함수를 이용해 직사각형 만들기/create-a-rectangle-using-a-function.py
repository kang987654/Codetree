n, m = map(int, input().split())

# Please write your code here.
def ret(n, m):
    for _ in range(n):
        for _ in range(m):
            print('1', end='')
        print()

ret(n, m)
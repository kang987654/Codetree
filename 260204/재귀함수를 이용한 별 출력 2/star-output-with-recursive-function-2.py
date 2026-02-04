n = int(input())

# Please write your code here.
def dec_inc_star(n):
    if n == 0:
        return
    print('* ' * n)
    dec_inc_star(n-1)
    print('* ' * n)

dec_inc_star(n)
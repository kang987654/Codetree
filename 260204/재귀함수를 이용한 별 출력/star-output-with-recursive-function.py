n = int(input())

# Please write your code here.
def stars(n):
    if n == 0:
        return
    stars(n-1)
    print('*' * n)

stars(n)
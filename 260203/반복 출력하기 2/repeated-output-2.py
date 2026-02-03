n = int(input())

# Please write your code here.
def say_hi(n):
    if n == 0:
        return
    say_hi(n-1)
    print('HelloWorld')

say_hi(n)
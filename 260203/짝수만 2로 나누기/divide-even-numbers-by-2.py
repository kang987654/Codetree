n = int(input())
arr = list(map(int, input().split()))

# Please write your code here.
def div_even(lst):
    for x in lst:
        if x % 2 == 0:
            print(int(x/2), end=' ')
        else:
            print(x, end=' ')

div_even(arr[:])
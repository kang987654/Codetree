n = int(input())
arr = list(map(int, input().split()))

# Please write your code here.
def my_abs(lst):
    for i in range(len(lst)):
        if lst[i] < 0:
            lst[i] *= -1
    return lst


for x in my_abs(arr):
    print(x, end=' ')
    
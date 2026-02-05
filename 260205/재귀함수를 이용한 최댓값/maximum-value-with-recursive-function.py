n = int(input())
arr = list(map(int, input().split()))

# Please write your code here.
def recursive_max(n):
    if n == 0:
        return 0

    next = recursive_max(n-1) 
    if arr[n-1] >= next:
        return arr[n-1]
    else:
        return next

print(recursive_max(n))
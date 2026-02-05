n = int(input())
arr = list(map(int, input().split()))

# Please write your code here.
def recursive_max(n, arr):
    if n == 0:
        return 0
    return arr[n-1] if arr[n-1] > recursive_max(n-1, arr) else recursive_max(n-1, arr)

print(recursive_max(n, arr))
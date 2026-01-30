n, m = map(int, input().split())

# Please write your code here.
def find_md(n, m):
    for i in range(min(n, m), 1, -1):
        if n % i == 0 and m % i == 0:
            return i
    return 1

print(find_md(n, m))
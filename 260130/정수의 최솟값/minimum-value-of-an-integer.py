a, b, c = map(int, input().split())

# Please write your code here.
def my_min(a, b, c):
    l = [a, b, c]
    return sorted(l)[0]

print(my_min(a, b, c))
a, b = map(int, input().split())

# Please write your code here.
def mul_or_add(a, b):
    return min(a, b)*2, max(a, b)+25

x, y = mul_or_add(a, b)
print(x, y)
a, b = map(int, input().split())

# Please write your code here.
def mul_or_add(a, b):
    if a < b:
        return a*2, b+25
    else:
        return a+25, b*2

x, y = mul_or_add(a, b)
print(x, y)
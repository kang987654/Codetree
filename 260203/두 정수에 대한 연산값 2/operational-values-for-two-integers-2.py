a, b = map(int, input().split())

# Please write your code here.
def mul_or_add(a, b):
    if a < b:
        return a+10, b*2
    else:
        return a*2, b+10

x, y = mul_or_add(a, b)
print(x, y)
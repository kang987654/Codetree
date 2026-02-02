a, o, c = input().split()
a = int(a)
c = int(c)

# Please write your code here.
def cal(a, o, c):
    if o == '+':
        return a + c
    if o == '-':
        return a - c
    if o == '/':
        return a / c
    if o == '*':
        return a * c
    return False

if cal(a, o, c):
    print(f'{a} {o} {c} = {cal(a, o, c)}')
else:
    print(False)
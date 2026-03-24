a = input()

# Please write your code here.
if '0' in a:
    a = list(a)
    for i in range(len(a)):
        if a[i] == '0':
            a[i] = '1'
            break
    a = ''.join(a)
else:
    a = a[:-1] + '0'

print(int(a, 2))
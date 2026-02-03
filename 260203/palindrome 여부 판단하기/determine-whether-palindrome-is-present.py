A = input()

# Please write your code here.
def is_pal(string):
    for i in range(len(string)):
        if string[i] != string[-(i+1)]:
            return False
    return True

if is_pal(A):
    print('Yes')
else:
    print('No')
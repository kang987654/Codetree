A = input()

# Please write your code here.
def is_diff_alpha(string):
    if len(set(string)) < 2:
        return False
    return True

if is_diff_alpha(A):
    print('Yes')
else:
    print('No')
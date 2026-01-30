a, b = map(int, input().split())

# Please write your code here.
def is_369(n):
    sn = str(n)
    if '3' in sn or '6' in sn or '9' in sn:
        return True

    return False
    
def game(a, b):
    cnt = 0
    for i in range(a, b+1):
        if i % 3 == 0 or is_369(i):
            cnt += 1
            
    return cnt


print(game(a, b))
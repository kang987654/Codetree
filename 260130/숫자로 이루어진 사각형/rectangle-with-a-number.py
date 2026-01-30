n = int(input())

# Please write your code here.
def num_ret(n):
    cnt = 0
    for _ in range(n):
        for _ in range(n):
            cnt += 1
            if cnt == 10:
                cnt = 1
            print(cnt, end=' ')
        print()
            
num_ret(n)

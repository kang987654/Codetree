N = int(input())
arr = [int(input()) for _ in range(N)]

# Please write your code here.
max_cnt = 0
cnt = 1
prev = 'z'

pm_arr = ['p' if a > 0 else 'm' for a in arr] + ['z']
for a in pm_arr:
    if a == prev:
        cnt += 1
    else:
        max_cnt = max(cnt, max_cnt)
        cnt = 1
        prev = a

print(max_cnt)

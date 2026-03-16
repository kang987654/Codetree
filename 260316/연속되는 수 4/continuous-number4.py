n = int(input())
arr = [int(input()) for _ in range(n)]

# Please write your code here.
max_cnt = 0
cnt = 1
prev = 1000

for a in arr + [0]:
    if a > prev:
        cnt += 1
        prev = a
    else:
        max_cnt = max(cnt, max_cnt)
        cnt = 1
        prev = a

print(max_cnt)

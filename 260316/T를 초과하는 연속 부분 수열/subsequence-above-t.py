n, t = map(int, input().split())
arr = list(map(int, input().split()))

# Please write your code here.
max_cnt = 0
cnt = 0
prev = -1
for a in arr + [-1]:
    if a > t:
        cnt += 1
    else:
        max_cnt = max(cnt, max_cnt)
        cnt = 0

print(max_cnt)

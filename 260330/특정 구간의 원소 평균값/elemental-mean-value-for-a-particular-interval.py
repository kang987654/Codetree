n = int(input())
arr = list(map(int, input().split()))

# Please write your code here.
cnt = 0
for i in range(n):
    for j in range(i+1, n+1):
        tmp = arr[i:j]

        if sum(tmp) % len(tmp) == 0 and (sum(tmp) // len(tmp)) in tmp:
            cnt += 1

print(cnt)

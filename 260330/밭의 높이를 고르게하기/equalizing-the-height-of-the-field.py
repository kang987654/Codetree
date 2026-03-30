N, H, T = map(int, input().split())
arr = list(map(int, input().split()))

# Please write your code here.
flatten = [abs(H-a) for a in arr]
answer = 200 * 10
for i in range(N-T+1):
    answer = min(sum(flatten[i:i+T]), answer)

print(answer)

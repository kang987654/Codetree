N, K = map(int, input().split())
num = [int(input()) for _ in range(N)]

# Please write your code here.
def find_bomb():
    global answer
    for i in range(N):
        if num[i] <= answer:
            continue

        for d in range(-K, K+1):
            if d == 0 or i+d < 0 or i+d >= N:
                continue
            elif num[i] == num[i+d]:
                answer = num[i]

answer = -1
find_bomb()

print(answer)

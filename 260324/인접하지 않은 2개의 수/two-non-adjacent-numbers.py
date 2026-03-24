n = int(input())
numbers = list(map(int, input().split()))

# Please write your code here.
answer = 0
for i in range(n):
    for j in range(i+2, n):
        answer = max(numbers[i]+numbers[j], answer)

print(answer)

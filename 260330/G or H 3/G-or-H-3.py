n, k = map(int, input().split())
x = []
c = []
for _ in range(n):
    pos, char = input().split()
    x.append(int(pos))
    c.append(char)

# Please write your code here.
scores = [0] * max(x)
for i, s in zip(x, c):
    scores[i-1] = 1 if s == 'G' else 2

answer = 0
for i in range(len(scores)-k):
    answer = max(sum(scores[i:i+k+1]), answer)

print(answer)

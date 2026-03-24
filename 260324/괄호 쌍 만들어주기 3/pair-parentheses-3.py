A = input()

# Please write your code here.
answer, o = 0, 0
for a in A:
    if a == '(':
        o += 1
    if a == ')':
        answer += o

print(answer)

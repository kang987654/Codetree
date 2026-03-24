A = input()

# Please write your code here.
cnt = 0
open_pair = 0
prev = '.'

for a in A:
    if a == '(' and a == prev:
        open_pair += 1
    if a == ')' and a == prev:
        cnt += open_pair
    prev = a

print(cnt)

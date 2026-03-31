n = int(input())
a, b, c = [], [], []
for _ in range(n):
    num, cnt1, cnt2 = map(int, input().split())
    a.append(num)
    b.append(cnt1)
    c.append(cnt2)

# Please write your code here.
from itertools import permutations

def game(guess, c1, c2):
    # c1: 숫자, 자리 같음, c2: 숫자 같음, 자리 다름
    for i in range(len(total)):
        s1, s2 = 0, 0
        for j in range(3):
            if guess[j] == total[i][j]:
                s1 += 1
            elif guess[j] in total[i]:
                s2 += 1
        if s1 == c1 and s2 == c2:
            valid[i] += 1


total = [i+j+k for i, j, k in permutations('123456789', 3)]
valid = [0] * len(total)

for i in range(n):
    game(str(a[i]), b[i], c[i])

print(valid.count(max(valid)))

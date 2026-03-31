N = int(input())
a1, b1, c1 = map(int, input().split())
a2, b2, c2 = map(int, input().split())

# Please write your code here.
if N <= 5:
    answer = N*N*N
else:
    answer = 5*5*5 * 2

    c1_1, c2_1, c3_1 = set(range(a1-2, a1+3)), set(range(b1-2, b1+3)), set(range(c1-2, c1+3))
    c1_2, c2_2, c3_2 = set(range(a2-2, a2+3)), set(range(b2-2, b2+3)), set(range(c2-2, c2+3))
    dup = len(c1_1 & c1_2) * len(c2_1 & c2_2) * len(c3_1 & c3_2)

    answer -= dup

print(answer)

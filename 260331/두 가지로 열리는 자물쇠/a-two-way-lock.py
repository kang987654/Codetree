N = int(input())
a1, b1, c1 = map(int, input().split())
a2, b2, c2 = map(int, input().split())

# Please write your code here.
if N <= 5:
    answer = N*N*N
else:
    answer = 5*5*5 * 2

    numbers = [N] + list(range(1, N))
    c_a1 = set([numbers[a1-2], numbers[a1-1], numbers[a1 % N], numbers[(a1+1) % N], numbers[(a1+2) % N]])
    c_b1 = set([numbers[b1-2], numbers[b1-1], numbers[b1 % N], numbers[(b1+1) % N], numbers[(b1+2) % N]])
    c_c1 = set([numbers[c1-2], numbers[c1-1], numbers[c1 % N], numbers[(c1+1) % N], numbers[(c1+2) % N]])

    c_a2 = set([numbers[a2-2], numbers[a2-1], numbers[a2 % N], numbers[(a2+1) % N], numbers[(a2+2) % N]])
    c_b2 = set([numbers[b2-2], numbers[b2-1], numbers[b2 % N], numbers[(b2+1) % N], numbers[(b2+2) % N]])
    c_c2 = set([numbers[c2-2], numbers[c2-1], numbers[c2 % N], numbers[(c2+1) % N], numbers[(c2+2) % N]])
    
    dup = len(c_a1 & c_a2) * len(c_b1 & c_b2) * len(c_c1 & c_c2)

    answer -= dup

print(answer)

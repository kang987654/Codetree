N = int(input())

# Please write your code here.
def seq(n):
    if n == 1:
        return 2
    if n == 2:
        return 4

    return (seq(n-1) * seq(n-2)) % 100

print(seq(N))
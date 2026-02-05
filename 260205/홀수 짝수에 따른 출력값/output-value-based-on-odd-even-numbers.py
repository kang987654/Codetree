N = int(input())

# Please write your code here.
def only_odd_or_even(n):
    if n == 1 or n == 2:
        return n
    return n + only_odd_or_even(n-2)

print(only_odd_or_even(N))
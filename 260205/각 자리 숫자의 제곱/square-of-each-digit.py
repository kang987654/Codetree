N = int(input())

# Please write your code here.
def digit_square_sum(n):
    if n < 10:
        return n**2
    return digit_square_sum(n//10) + (n % 10)**2

print(digit_square_sum(N))
a, b, c = map(int, input().split())

# Please write your code here.
def sum_of_digit(n):
    if n < 10:
        return n

    return sum_of_digit(n // 10) + n % 10

print(sum_of_digit(a*b*c))
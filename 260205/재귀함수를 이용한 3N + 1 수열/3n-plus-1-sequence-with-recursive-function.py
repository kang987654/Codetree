n = int(input())

# Please write your code here.
def count_seq(n):
    if n == 1:
        return 0

    if n % 2 == 0:
        n = int(n/2)
    else:
        n = n*3 + 1
    
    return count_seq(n) + 1


print(count_seq(n))
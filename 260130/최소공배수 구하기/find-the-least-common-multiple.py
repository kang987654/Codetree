n, m = map(int, input().split())

# Please write your code here.
def find_mm(n, m):
    for i in range(max(n, m), 10000):
        if i % n == 0 and i % m == 0:
            print(i)
            break

find_mm(n, m)
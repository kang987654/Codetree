a, b, c, d = map(int, input().split())

# Please write your code here.
def h_to_min(h, m):
    return 60*h + m

print(h_to_min(c, d) - h_to_min(a, b))

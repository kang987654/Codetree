n1, n2 = map(int, input().split())
a = list(map(int, input().split()))
b = list(map(int, input().split()))

# Please write your code here.
def is_in(a, b):
    st_a, st_b = ',', ','
    for w in a:
        st_a += (str(w) + ',')
    for w in b:
        st_b += (str(w) + ',')
    
    return st_b in st_a

if is_in(a, b):
    print('Yes')
else:
    print('No')
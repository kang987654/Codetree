a, b, c = map(int, input().split())

# Please write your code here.
def d_to_h(d):
    return d * 24

def h_to_min(h):
    return h * 60

_1111 = h_to_min(d_to_h(11) + 11) + 11
q = h_to_min(d_to_h(a) + b) + c

answer = q - _1111 if q >= _1111 else -1
print(answer)
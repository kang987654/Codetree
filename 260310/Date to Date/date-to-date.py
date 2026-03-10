m1, d1, m2, d2 = map(int, input().split())

# Please write your code here.
days = [0, 31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]

def m_to_d(m, d):
    return sum(days[:m]) + d

print(m_to_d(m2, d2) - m_to_d(m1, d1) + 1)

m1, d1, m2, d2 = map(int, input().split())
A = input()

# Please write your code here.
day7 = ['Mon', 'Tue', 'Wed', 'Thu', 'Fri', 'Sat', 'Sun']
days = [0, 31, 29, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]

def m_to_d(m, d):
    return sum(days[:m]) + d

dd = m_to_d(m2, d2) - m_to_d(m1, d1) + 1
weeks, remain = dd // 7, dd % 7

print(weeks + (A in day7[:remain]))

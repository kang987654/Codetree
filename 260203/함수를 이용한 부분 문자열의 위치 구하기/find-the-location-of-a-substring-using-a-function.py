text = input()
pattern = input()

# Please write your code here.
def is_in(t, p):
    for i in range(len(t)-len(p)+1):
        if t[i:i+len(p)] == p:
            return i
    return -1

print(is_in(text, pattern))
N, B = map(int, input().split())

# Please write your code here.
jinsu = ''
while N >= B:
    jinsu = str(N%B) + jinsu
    N = N // B

print(str(N) + jinsu)

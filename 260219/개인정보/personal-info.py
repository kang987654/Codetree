n = 5
name = []
height = []
weight = []

for _ in range(n):
    n, h, w = input().split()
    name.append(n)
    height.append(int(h))
    weight.append(float(w))

# Please write your code here.
infos = [(n, h, w) for n, h, w in zip(name, height, weight)]
print('name')
for n, h, w in sorted(infos, key=lambda info: info[0]):
    print(n, h, w)
print()
print('height')
for n, h, w in sorted(infos, key=lambda info: -info[1]):
    print(n, h, w)

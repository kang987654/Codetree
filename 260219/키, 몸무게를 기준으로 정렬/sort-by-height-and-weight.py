n = int(input())
name = []
height = []
weight = []
for _ in range(n):
    n_i, h_i, w_i = input().split()
    name.append(n_i)
    height.append(int(h_i))
    weight.append(int(w_i))

# Please write your code here.
infos = [(n, h, w) for n, h, w in zip(name, height, weight)]
for n, h, w in sorted(infos, key=lambda info: (info[1], -info[2])):
    print(n, h, w)
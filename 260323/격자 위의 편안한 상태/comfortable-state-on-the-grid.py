n, m = map(int, input().split())
points = [tuple(map(int, input().split())) for _ in range(m)]

# Please write your code here.
near = [
    (-1, +0),
    (+1, +0),
    (+0, -1),
    (+0, +1)
]
arr = [[0] * n for _ in range(n)]


def paint(r, c):
    arr[r][c] = 1

    tmp = []
    for i, j in near:
        if 0 <= r+i < n and 0 <= c+j < n:
            tmp.append(arr[r+i][c+j])

    if sum(tmp) == 3:
        return 1
    else:
        return 0


for r, c in points:
    r, c = r-1, c-1

    print(paint(r, c))

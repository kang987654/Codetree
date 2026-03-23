n = int(input())
grid = [list(input()) for _ in range(n)]
k = int(input())

# Please write your code here.
head = {
    'U': (-1, +0),
    'D': (+1, +0),
    'L': (+0, -1),
    'R': (+0, +1)
}

if k <= n:
    laser_r, laser_c = 0, k - 1
    laser_d = 'D'
elif k <= 2 * n:
    laser_r, laser_c = k - (n + 1), n - 1
    laser_d = 'L'
elif k <= 3 * n:
    laser_r, laser_c = n - 1, 3 * n - k
    laser_d = 'U'
else:
    laser_r, laser_c = 4 * n - k, 0
    laser_d = 'R'

cnt = 0
while 0 <= laser_r < n and 0 <= laser_c < n:
    cnt += 1
    if grid[laser_r][laser_c] == '/':
        if laser_d == 'U':
            laser_d = 'R'
        if laser_d == 'D':
            laser_d = 'L'
        if laser_d == 'L':
            laser_d = 'D'
        if laser_d == 'R':
            laser_d = 'U'
    else:   # grid[laser_r][laser_c] == '\\':
        if laser_d == 'U':
            laser_d = 'L'
        if laser_d == 'D':
            laser_d = 'R'
        if laser_d == 'L':
            laser_d = 'U'
        if laser_d == 'R':
            laser_d = 'D'

    dr, dc = head[laser_d]
    laser_r += dr
    laser_c += dc

print(cnt)

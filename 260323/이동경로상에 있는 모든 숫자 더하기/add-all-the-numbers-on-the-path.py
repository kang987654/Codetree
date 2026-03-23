N, T = map(int, input().split())
str = input()
board = [list(map(int, input().split())) for _ in range(N)]

# Please write your code here.
dir = [
    (-1, +0),
    (+0, +1),
    (+1, +0),
    (+0, -1)
]

r, c = N//2, N//2
answer = board[r][c]
d = 0
for s in str:
    if s == 'L':
        d = (d+4 - 1) % 4
    if s == 'R':
        d = (d+1) % 4
    if s == 'F':
        dr, dc = dir[d]
        if 0 <= r + dr < N and 0 <= c + dc < N:
            r += dr
            c += dc
            answer += board[r][c]

print(answer)

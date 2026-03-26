board = [list(map(int, input().split())) for _ in range(19)]

# Please write your code here.
def check_is_winner(i, j, v):
    # |
    for d in range(-2, 3):
        if board[i+d][j] != v:
            break
        if d == 2:
            return True
    # /
    for d in range(-2, 3):
        if board[i+d][j-d] != v:
            break
        if d == 2:
            return True
    # ㅡ
    for d in range(-2, 3):
        if board[i][j+d] != v:
            break
        if d == 2:
            return True
    # 역 /
    for d in range(-2, 3):
        if board[i+d][j+d] != v:
            break
        if d == 2:
            return True

    return False


def omok():
    for i in range(2, 19-2):
        for j in range(2, 19-2):
            if board[i][j] != 0 and check_is_winner(i, j, board[i][j]):
                return board[i][j], i+1, j+1
    return 0, 0, 0

winner, r, c = omok()
print(winner)
if winner:
    print(r, c)

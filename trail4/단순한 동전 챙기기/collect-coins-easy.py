n = int(input())
grid = [list(input()) for _ in range(n)]

start_x, start_y = 0, 0
end_x, end_y = 0, 0
coins = []

# S, E 위치 및 동전 위치 수집
for r in range(n):
    for c in range(n):
        if grid[r][c] == 'S':
            start_x, start_y = r, c
        elif grid[r][c] == 'E':
            end_x, end_y = r, c
        elif grid[r][c] != '.':
            coins.append((int(grid[r][c]), r, c))

# 동전 번호 오름차순 정렬
coins.sort()

min_m = float('inf')


def dist(x1, y1, x2, y2):
    return abs(x1 - x2) + abs(y1 - y2)


# idx: 확인할 동전 번호, (last_x, last_y): 직전 위치, c: 모은 동전 수, m: 누적 이동 거리
def dfs(idx, last_x, last_y, c, m):
    global min_m

    # 1. 동전 3개를 모두 모으면 도착지 'E'까지 거리를 더하고 최솟값 갱신
    if c == 3:
        min_m = min(min_m, m + dist(last_x, last_y, end_x, end_y))
        return

    # 2. 모든 동전을 다 확인했으면 종료
    if idx == len(coins):
        return

    # 선택지 1: 현재 동전을 줍는 경우
    num, cx, cy = coins[idx]
    dfs(idx + 1, cx, cy, c + 1, m + dist(last_x, last_y, cx, cy))

    # 선택지 2: 현재 동전을 건너뛰는 경우
    dfs(idx + 1, last_x, last_y, c, m)


# 탐색 시작: 0번 동전부터, 시작점 (start_x, start_y), 동전 0개, 거리 0
dfs(0, start_x, start_y, 0, 0)

print(min_m if min_m != float('inf') else -1)
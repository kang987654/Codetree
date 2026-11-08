import sys

# 입력 처리
n, m = map(int, sys.stdin.readline().split())
points = [tuple(map(int, sys.stdin.readline().split())) for _ in range(n)]

selected = []
ans = float('inf')

# 두 점 사이의 거리 제곱 계산
def calc_dist_sq(p1, p2):
    return (p1[0] - p2[0]) ** 2 + (p1[1] - p2[1]) ** 2

# 선택된 M개의 점들 중 가장 먼 두 점 사이의 거리 제곱 구하기
def get_max_dist():
    max_d = 0
    for i in range(m):
        for j in range(i + 1, m):
            max_d = max(max_d, calc_dist_sq(selected[i], selected[j]))
    return max_d

# 백트래킹으로 M개의 점 선택
def choose(idx, cnt):
    global ans
    
    # M개를 모두 선택한 경우
    if cnt == m:
        ans = min(ans, get_max_dist())
        return
    
    # 끝까지 탐색했거나, 남은 점을 다 골라도 M개가 안 되는 경우 (가지치기)
    if idx == n or (n - idx) < (m - cnt):
        return

    # 현재 점(idx)을 선택하는 경우
    selected.append(points[idx])
    choose(idx + 1, cnt + 1)
    selected.pop()

    # 현재 점(idx)을 선택하지 않는 경우
    choose(idx + 1, cnt)

choose(0, 0)
print(ans)
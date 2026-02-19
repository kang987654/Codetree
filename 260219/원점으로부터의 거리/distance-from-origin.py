n = int(input())
points = [(int(i), tuple(map(int, input().split()))) for i in range(n)]

# Please write your code here.
for i, p in sorted(points, key=lambda point: abs(point[1][0])+abs(point[1][1])):
    print(i+1)

N, B = map(int, input().split())
P = [int(input()) for _ in range(N)]

# Please write your code here.
def teacher(i, budget, halfed):
    global max_students
    
    if i == N:
        max_students = N
        return

    if not halfed and budget + P[i]//2 <= B:
        max_students = i+1
        teacher(i+1, budget + P[i]//2, True)
    if budget + P[i] <= B:
        teacher(i+1, budget + P[i], halfed)

P.sort()
max_students = 0
teacher(0, 0, False)

print(max_students)

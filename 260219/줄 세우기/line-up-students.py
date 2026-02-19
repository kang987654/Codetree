n = int(input())
students = [tuple(map(int, input().split())) + (i + 1,) for i in range(n)]

# Please write your code here.
for h, w, n in sorted(students, key=lambda student: (-student[0], -student[1])):
    print(h, w, n)

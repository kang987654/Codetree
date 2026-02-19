n = int(input())
name = []
korean = []
english = []
math = []

for _ in range(n):
    student_info = input().split()
    name.append(student_info[0])
    korean.append(int(student_info[1]))
    english.append(int(student_info[2]))
    math.append(int(student_info[3]))

# Please write your code here.
students = [(n, k, e, m) for n, k, e, m in zip(name, korean, english, math)]
for n, k, e, m in sorted(students, key=lambda student: (-student[1], -student[2], -student[3])):
    print(n, k, e, m)

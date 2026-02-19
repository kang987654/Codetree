n = int(input())

name = []
score1 = []
score2 = []
score3 = []

for _ in range(n):
    student_input = input().split()
    name.append(student_input[0])
    score1.append(int(student_input[1]))
    score2.append(int(student_input[2]))
    score3.append(int(student_input[3]))

# Please write your code here.
students = [(n, s1, s2, s3) for n, s1, s2, s3 in zip(name, score1, score2, score3)]
for n, s1, s2, s3 in sorted(students, key=lambda student: sum(student[1:])):
    print(n, s1, s2, s3)

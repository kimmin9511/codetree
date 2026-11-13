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


class info :
    def __init__(self, a, b, c, d) :
        self.name = a
        self.score1 = b
        self.score2 = c
        self.score3 = d


students = []

for i in range(n) :
    students.append(info(name[i], score1[i], score2[i], score3[i]))

students.sort(key = lambda x : x.score1 + x.score2 + x.score3)

for student in students :
    print(student.name, student.score1, student.score2, student.score3)
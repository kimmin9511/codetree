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


class info :
    def __init__(self, a, b, c, d) :
        self.name = a
        self.korean = b
        self.english = c
        self.math = d


students = []

for i in range(n) :
    students.append(info(name[i], korean[i], english[i], math[i]))

students.sort(key = lambda x : (-x.korean, -x.english, -x.math))

for student in students :
    print(student.name, student.korean, student.english, student.math)
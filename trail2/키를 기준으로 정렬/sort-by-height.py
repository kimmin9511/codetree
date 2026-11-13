n = int(input())
name = []
height = []
weight = []

for _ in range(n):
    n_i, h_i, w_i = input().split()
    name.append(n_i)
    height.append(int(h_i))
    weight.append(int(w_i))


class info :
    def __init__(self, a, b, c) :
        self.name = a
        self.height = b
        self.weight = c


students = []

for i in range(n) :
    students.append(info(name[i], height[i], weight[i]))

students.sort(key = lambda x : x.height)

for student in students :
    print(student.name, student.height, student.weight)
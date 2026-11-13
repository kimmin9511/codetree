k = 5
name = []
height = []
weight = []

for _ in range(k):
    n, h, w = input().split()
    name.append(n)
    height.append(int(h))
    weight.append(float(w))


class info :
    def __init__(self, a, b, c) :
        self.name = a
        self.height = b
        self.weight = c


students = []
for i in range(k) :
    students.append(info(name[i], height[i], weight[i]))

students.sort(key = lambda x : x.name)
print("name")
for student in students :
    print(student.name, student.height, student.weight)

print()

students.sort(key = lambda x : -x.height)
print('height')
for student in students :
    print(student.name, student.height, student.weight)
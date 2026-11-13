n = int(input())
students = [
    (h, w, i + 1)
    for i, (h, w) in enumerate([tuple(map(int, input().split())) for _ in range(n)])
]

class info :
    def __init__(self, a, b, c) :
        self.height = a
        self.weight = b
        self.num = c


_list = []
for i in range(n) :
    _list.append(info(students[i][0], students[i][1], students[i][2]))

_list.sort(key = lambda x : (x.height, -x.weight))

for student in _list :
    print(student.height, student.weight, student.num)
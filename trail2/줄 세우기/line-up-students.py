n = int(input())
students = [tuple(map(int, input().split())) + (i + 1,) for i in range(n)]


class info :
    def __init__(self, a, b, c) :
        self.h = a
        self.w = b
        self.num = c


_list = []
for i in range(n) :
    _list.append(info(students[i][0], students[i][1], students[i][2]))

_list.sort(key = lambda x : (-x.h, -x.w, x.num))

for student in _list :
    print(student.h, student.w, student.num)

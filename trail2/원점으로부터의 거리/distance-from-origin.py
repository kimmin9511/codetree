n = int(input())
points = [(int(i), tuple(map(int, input().split()))) for i in range(n)]


class info :
    def __init__(self, a, b, c) :
        self.num = a
        self.dot1 = b
        self.dot2 = c


_list = []

for i in range(n) :
    _list.append(info(points[i][0], points[i][1][0], points[i][1][1]))

_list.sort(key = lambda x : abs(x.dot1) + abs(x.dot2))

for student in _list:
    print(student.num+1)


n = int(input())
x1, y1, x2, y2 = [], [], [], []
for _ in range(n):
    a, b, c, d = map(int, input().split())
    x1.append(a)
    y1.append(b)
    x2.append(c)
    y2.append(d)

offset = 100

_list = [
    [0 for _ in range(2*offset)]
    for _ in range(2*offset)
]

for i in range(n) :
    for start in range(x1[i] + offset, x2[i] + offset) :
        for end in range(y1[i] + offset, y2[i] + offset) :
            _list[start][end] += 1

cnt = 0
for row in _list :
    for elem in row :
        if elem >= 1 :
            cnt += 1
    
print(cnt)
            

n = int(input())
x1, y1, x2, y2 = [], [], [], []
for _ in range(n):
    a, b, c, d = map(int, input().split())
    x1.append(a)
    y1.append(b)
    x2.append(c)
    y2.append(d)

offset = 100

arr = [
    [0 for _ in range(2*offset)]
    for _ in range(2*offset)
]

for k in range(n) :
    for i in range(x1[k], x2[k]) :
        for j in range(y1[k], y2[k]) :
            if k % 2 == 0 :
                arr[i][j] = 'red'

            elif k % 2 == 1 :
                arr[i][j] = 'blue'

cnt = 0
for row in arr :
    for elem in row :
        if elem == 'blue' :
            cnt += 1

print(cnt)
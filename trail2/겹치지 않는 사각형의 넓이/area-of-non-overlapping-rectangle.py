x1 = [0] * 3
y1 = [0] * 3
x2 = [0] * 3
y2 = [0] * 3

x1[0], y1[0], x2[0], y2[0] = map(int, input().split())
x1[1], y1[1], x2[1], y2[1] = map(int, input().split())
x1[2], y1[2], x2[2], y2[2] = map(int, input().split())

offset = 1000

arr = [
    [0 for _ in range(2*offset)]
    for _ in range(2*offset)
]

for i in range(2) :
    for x_num in range(x1[i], x2[i]) :
        for y_num in range(y1[i], y2[i]) :
            arr[x_num+offset][y_num+offset] += 1

for x_num in range(x1[2], x2[2]) :
    for y_num in range(y1[2], y2[2]) :
        arr[x_num+offset][y_num+offset] -= 1

cnt = 0
for row in arr :
    for elem in row :
        if elem == 1 :
            cnt += 1

print(cnt)


            
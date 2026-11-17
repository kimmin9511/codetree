n = int(input())
points = [tuple(map(int, input().split())) for _ in range(n)]
x, y = zip(*points)
x, y = list(x), list(y)

offset = 100

arr = [
    [0 for _ in range(2*offset)]
    for _ in range(2*offset)
]

for i in range(n) :
    for x_num in range(x[i], x[i] + 8) :
        for y_num in range(y[i], y[i] + 8) :
            arr[x_num][y_num] += 1

cnt = 0
for row in arr :
    for elem in row :
        if elem >= 1 :
            cnt += 1

print(cnt)
x1, y1, x2, y2 = [0] * 2, [0] * 2, [0] * 2, [0] * 2
x1[0], y1[0], x2[0], y2[0] = map(int, input().split())
x1[1], y1[1], x2[1], y2[1] = map(int, input().split())


offset = 1000

arr = [
    [0 for _ in range(2*offset)]
    for _ in range(2*offset)
]

for i in range(x1[0] + offset, x2[0] + offset) :
    for j in range(y1[0] + offset, y2[0] + offset) :
        arr[i][j] += 1

for i in range(x1[1] + offset, x2[1] + offset) :
    for j in range(y1[1] + offset, y2[1] + offset) :
        arr[i][j] -= 1

row_num = []
col_num = []

for i in range(2*offset) :
    for j in range(2*offset) :
        if arr[i][j] == 1 :
            row_num.append(i)
            col_num.append(j)

if len(row_num) == 0 and len(col_num) == 0 :
    print(0)

else :
    print((max(row_num)- (min(row_num)-1)) * (max(col_num) - (min(col_num) - 1)))

            
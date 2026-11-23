n, m = map(int, input().split())
points = [tuple(map(int, input().split())) for _ in range(m)]

arr = [
    [0 for _ in range(n)]
    for _ in range(n)
]

dxs, dys = [0, 1, 0, -1], [1, 0, -1, 0]

def in_range(a, b) :
    return 0<= a < n and 0 <= b < n

for i in range(m) :
    cnt = 0

    x, y = points[i][0]-1, points[i][1]-1
    arr[x][y] = 1
    
    for j in range(4) :
        nx, ny = x + dxs[j], y + dys[j]

        if in_range(nx, ny) and arr[nx][ny] == 1 :
            cnt += 1

    if cnt == 3 :
        print(1)
        
    else :
        print(0)


    










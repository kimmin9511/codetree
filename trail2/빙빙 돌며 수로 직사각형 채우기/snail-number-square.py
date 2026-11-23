n, m = map(int, input().split())
arr = [[0] * m for _ in range(n)]

x, y = 0, 0
dxs, dys = [0, 1, 0, -1], [1, 0, -1, 0]

arr[x][y] = 1

dir_num = 0

def in_range(a, b) :
    return 0 <= a < n and 0 <= b < m


for i in range(2, n*m + 1) :
    nx, ny = x + dxs[dir_num], y + dys[dir_num]

    if not in_range(nx, ny) or arr[nx][ny] != 0 :
        dir_num = (dir_num+1) % 4

    x, y = x + dxs[dir_num], y + dys[dir_num]
    arr[x][y] = i

for row in arr :
    for elem in row :
        print(elem, end=" ")
    print()
        

    



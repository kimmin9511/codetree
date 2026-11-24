n = int(input())
grid = [[0] * n for _ in range(n)]

x, y = n-1, n-1
grid[x][y] = n*n

dxs, dys = [0, -1, 0, 1], [-1, 0, 1, 0]

dir_num = 0

def in_range(a, b) :
    return 0 <= a < n and 0 <= b < n


for i in range(n*n-1, 0, -1) :
    nx, ny = x + dxs[dir_num] , y + dys[dir_num]

    if not in_range(nx, ny) or grid[nx][ny] != 0 :
        dir_num = (dir_num + 1) % 4

    x, y = x + dxs[dir_num] , y + dys[dir_num]
    grid[x][y] = i

for row in grid :
    for elem in row :
        print(elem, end=" ")

    print()
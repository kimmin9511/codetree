n, m = map(int, input().split())

_list = [
    [0 for _ in range(m)]
    for _ in range(n)
]

x, y = 0, 0

_list[x][y] = 1

dxs , dys = [1, 0, -1, 0], [0, -1, 0, 1]

dir_num = 0

def in_range(a, b) :
    return 0 <= a < n and 0 <= b < m

for i in range(2, n*m+1) :
    nx, ny = x + dxs[dir_num], y + dys[dir_num]

    if not in_range(nx, ny) or _list[nx][ny] != 0 :
        dir_num = (dir_num+3) % 4

    x, y = x + dxs[dir_num], y + dys[dir_num] 
    _list[x][y] = i

for row in _list :
    for elem in row :
        print(elem, end=" ")

    print()



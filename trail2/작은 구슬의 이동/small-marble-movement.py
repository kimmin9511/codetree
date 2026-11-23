n, t = map(int, input().split())
r, c, d = input().split()
r, c = int(r), int(c)

dxs, dys = [-1, 0, 0, 1], [0, 1, -1, 0]

mapper = {
    'U' : 0,
    'R' : 1,
    'L' : 2,
    'D' : 3
}

dir_num = mapper[d]

x, y = r-1, c-1

def in_range(a, b) :
    return a >= 0 and a < n and b >= 0 and b < n

for _ in range(t) :
    nx, ny = x + dxs[dir_num], y + dys[dir_num]

    if in_range(nx, ny) :
        x, y = nx, ny

    else :
        dir_num = 3 - dir_num

print(x+1, y+1)
N, T = map(int, input().split())
str = input()
board = [list(map(int, input().split())) for _ in range(N)]

sum = 0

x, y = N//2, N//2
sum += board[x][y]

dxs, dys = [-1, 0, 1, 0], [0, 1, 0, -1]
dir_num = 0

def in_range(a, b) :
    return 0<=a<N and 0<=b<N


for word in str :
    if word == 'L' :
        dir_num = (dir_num + 3) % 4

    elif word == 'R' :
        dir_num = (dir_num+1) % 4

    elif word == 'F' :
        nx, ny = x + dxs[dir_num] , y + dys[dir_num]

        if in_range(nx, ny) :
            x, y = x + dxs[dir_num] , y + dys[dir_num]
            sum += board[x][y]

print(sum)
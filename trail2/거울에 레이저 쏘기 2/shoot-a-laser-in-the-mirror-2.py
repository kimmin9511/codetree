n = int(input())
arr = [list(input()) for _ in range(n)]
k = int(input())

cnt = 0
dxs, dys = [0, 1, 0, -1], [1, 0, -1, 0]
dir_num = 0
x, y = 0, 0
move = True

def in_range(a,b) :
    return 0<=a<n and 0<=b<n


if 1 <= k <= n :
    x, y = 0, k-1
    dir_num = 1

elif n+1 <= k <= 2*n :
    x, y = k-n-1, n-1
    dir_num = 2

elif 2*n+1 <= k <= 3*n :
    x, y = n-1, 3*n-k
    dir_num = 3

elif 3*n+1 <= k <= 4*n :
    x, y = 4*n-k, 0
    dir_num = 0

while move :
    
    if arr[x][y] == '/' :
        cnt += 1

        if dir_num % 2 == 0:
            dir_num = (dir_num + 3) % 4
        else:
            dir_num = (dir_num + 1) % 4


    elif arr[x][y] == '\\' :
        cnt += 1

        if dir_num % 2 == 0:
            dir_num = (dir_num + 1) % 4
        else:
            dir_num = (dir_num + 3) % 4

    x, y = x + dxs[dir_num], y + dys[dir_num]

    if not in_range(x,y) :
        move = False

print(cnt)


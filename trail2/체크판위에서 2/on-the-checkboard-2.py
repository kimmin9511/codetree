R, C = map(int, input().split())
grid = [list(input().split()) for _ in range(R)]

x, y = 0, 0
cnt = 0

for i in range(x+1, R) :
    for j in range(y+1, C) :
        if grid[x][y] != grid[i][j] :

            for k in range(i+1, R) :
                for l in range(j+1, C) :
                    if grid[i][j] != grid[k][l] :

                        if grid[k][l] != grid[R-1][C-1] and R-1 >= k+1 and C-1 >= l+1 :
                            cnt += 1

print(cnt)



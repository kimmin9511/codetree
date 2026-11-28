N, M = map(int, input().split())
arr = [input() for _ in range(N)]

def in_range(a,b) :
    return 0<=a<N and 0<=b<M

dxs, dys = [-1, -1, 0, 1, 1, 1, 0, -1], [0, 1, 1, 1, 0, -1, -1, -1]

cnt = 0
solve = 0

for i in range(N) :
    for j in range(M) :
        if arr[i][j] == 'L' :
            
            for dx, dy in zip(dxs, dys) :
                for k in range(2) :
                    ni, nj = i + dx*(k+1), j + dy*(k+1)

                    if in_range(ni, nj) and arr[ni][nj] == 'E' :
                        solve += 1

                if solve == 2 :
                    cnt += 1

                solve = 0

print(cnt)




n = int(input())
grid = [list(map(int, input().split())) for _ in range(n)]

dxs, dys = [0, 1, 0, -1], [1, 0, -1, 0]

def in_range(a, b) :
    return a >= 0 and a < n and b >= 0 and b < n

cnt = 0

for i in range(n) :
    for j in range(n) :
        x, y = i, j
        
        solve = 0
        
        for dx, dy in zip(dxs, dys) :
            nx, ny = x + dx, y + dy
            
            
            if in_range(nx, ny) and grid[nx][ny] == 1:
                solve += 1

        
        if solve >= 3 :
            cnt += 1

print(cnt)

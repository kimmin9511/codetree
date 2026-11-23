N = int(input())
moves = [tuple(input().split()) for _ in range(N)]
dir = [move[0] for move in moves]
dist = [int(move[1]) for move in moves]

dxs, dys = [1, 0, -1, 0], [0, -1, 0, 1]

x, y = 0, 0

mapper = {
    'E' : 0,
    'S' : 1,
    'W' : 2,
    'N' : 3
}

solve = -1
time = 0


for num in range(N) :        
    dir_num = mapper[dir[num]]
    
    for _ in range(dist[num]) :
        x, y = x + dxs[dir_num], y + dys[dir_num]
        time += 1

        if x == 0 and y == 0 :
            solve = time
            break

    if solve == time :
        break

print(solve)
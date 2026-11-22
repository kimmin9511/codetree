n = int(input())
moves = [tuple(input().split()) for _ in range(n)]
dir = [move[0] for move in moves]
dist = [int(move[1]) for move in moves]

dx, dy = [1, 0, -1, 0], [0, -1, 0, 1]
x, y = 0, 0

for i in range(n) :
    if dir[i] == 'E' :
        x, y = x + dist[i]*dx[0], y + dist[i]*dy[0]

    elif dir[i] == 'S' :
        x, y = x + dist[i]*dx[1], y + dist[i]*dy[1]

    elif dir[i] == 'W' :
        x, y = x + dist[i]*dx[2], y + dist[i]*dy[2]

    elif dir[i] == 'N' :
        x, y = x + dist[i]*dx[3], y + dist[i]*dy[3]

print(x, y)



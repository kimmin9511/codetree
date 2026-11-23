dirs = input()

x, y = 0, 0

dir_num = 3
dx, dy = [1, 0, -1, 0], [0, -1, 0, 1]

for word in dirs :
    if word == 'L' :
        dir_num = (dir_num+3) % 4

    elif word == 'R' :
        dir_num = (dir_num+1) % 4

    elif word == 'F' :
        x, y = x + dx[dir_num], y + dy[dir_num]

print(x, y)


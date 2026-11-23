commands = input()

x, y = 0, 0

dir_num = 3

dxs, dys = [1, 0, -1, 0], [0, -1, 0, 1] 

solve = -1

time = 0

for word in commands :
    if word == 'L' :
        dir_num = (dir_num + 3) % 4

    elif word == 'R' :
        dir_num = (dir_num + 1) % 4

    elif word == 'F' :
        x, y = x + dxs[dir_num], y + dys[dir_num]

    time += 1

    if time != 1 and (x == 0 and y == 0) :
        solve = time
        break

print(solve)
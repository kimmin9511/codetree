n = int(input())
commands = [tuple(input().split()) for _ in range(n)]
x = []
dir = []
for num, direction in commands:
    x.append(int(num))
    dir.append(direction)

offset = 100

_list = [0] * (2*n*offset + 1)
num = n*offset

for i in range(n) :
    if dir[i] == 'R' :
        for j in range(num, num + x[i]) :
            _list[j] = 'black'
        num += x[i] - 1

    elif dir[i] == 'L' :
        for j in range(num - x[i] + 1, num + 1) :
            _list[j] = 'white'
        num -= x[i] - 1

white_cnt = 0
black_cnt = 0

for word in _list :
    if word == 'black' :
        black_cnt += 1
    elif word == 'white' :
        white_cnt += 1

print(white_cnt, black_cnt)
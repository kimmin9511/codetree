n = int(input())
commands = [tuple(input().split()) for _ in range(n)]
x = []
dir = []
for num, direction in commands:
    x.append(int(num))
    dir.append(direction)


offset = 100
num = n*100 + 1
_list = [0] * (2*n*100 + 1)
_find1 = [0] * (2*n*100 + 1)
_find2 = [0] * (2*n*100 + 1)

for i in range(n) :
    if dir[i] == 'R' :
        for j in range(num, num + x[i]) :
            _list[j] = 'black'
            _find1[j] += 1

        num += x[i] - 1

    elif dir[i] == 'L' :
        for j in range(num - x[i] + 1, num + 1) :
            _list[j] = 'white'
            _find2[j] += 1

        num -= x[i] - 1

for solve in range(2*n*100 + 1) :
    if _find1[solve] >= 2 and _find2[solve] >= 2 :
        _list[solve] = 'gray'


white_cnt = 0
black_cnt = 0
gray_cnt = 0

for k in _list :
    if k == 'white' :
        white_cnt += 1

    elif k == 'black' :
        black_cnt += 1
    
    elif k == 'gray' :
        gray_cnt += 1

print(white_cnt, black_cnt, gray_cnt)
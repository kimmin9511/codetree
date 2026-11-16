n, k = map(int, input().split())
commands = [tuple(map(int, input().split())) for _ in range(k)]

_list = [0] * (n+1)

for i in commands :
    if i[0] == i[1] :
        _list[i[0]] += 1

    else :
        for j in range(i[0] , i[1] + 1) :
            _list[j] += 1

max_num = 0

for k in _list[1:] :
    if k >= max_num :
        max_num = k

print(max_num)


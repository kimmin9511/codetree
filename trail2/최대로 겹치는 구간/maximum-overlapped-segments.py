n = int(input())
segments = [tuple(map(int, input().split())) for _ in range(n)]

offset = 100

_list = [0] * (offset*2) 

for i in segments :
    for j in range(i[0] + offset, i[1] + offset) :
        _list[j] += 1


print(max(_list))
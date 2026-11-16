n = int(input())
segments = [tuple(map(int, input().split())) for _ in range(n)]

offset = 100

_list = [0] * (offset+1)

for i in segments :
    for j in range(i[0], i[1]+1) :
        _list[j] += 1


print(max(_list))
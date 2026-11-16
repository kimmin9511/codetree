n = int(input())
segments = [list(map(int, input().split())) for _ in range(n)]

offset = 100

_list = [0] * (offset*2) 

# min_num = 0
# for num in segments :
#     if num[0] < min_num :
#         min_num = num[0]
    

for i in segments :
    for j in range(i[0], i[1]) :
        _list[j] += 1


max_num = 0

for k in _list[1:] :
    if k > max_num :
        max_num = k

print(max_num)
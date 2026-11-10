n = int(input())
arr = list(map(int, input().split()))

_list = []

for i in range(n) :
    _list.append(arr[i])
    if i % 2 == 0 :
        _list.sort()
        print(_list[int(i-(i/2))], end=" ")

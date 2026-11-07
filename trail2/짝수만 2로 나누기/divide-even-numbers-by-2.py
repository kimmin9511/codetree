n = int(input())
arr = list(map(int, input().split()))


def modify(_list) :
    for i in range(len(_list)) :
        if _list[i] % 2 == 0 :
            _list[i] = int(_list[i] / 2)

    for j in _list :
        print(j, end=" ")

    
modify(arr)


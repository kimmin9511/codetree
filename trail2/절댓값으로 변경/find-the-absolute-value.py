n = int(input())
arr = list(map(int, input().split()))


def modify(num, _list) :
    for i in range(num) :
        if _list[i] < 0 :
            _list[i] = -1*(_list[i])


modify(n, arr)

for j in arr :
    print(j, end=" ")

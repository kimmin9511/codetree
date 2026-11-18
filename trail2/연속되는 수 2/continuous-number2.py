n = int(input())
arr = [int(input()) for _ in range(n)]

cnt = 0
_list = []

for i in range(n) :

    if i == 0 or arr[i] == arr[i-1] :
        cnt += 1

        if i == n-1 :
            _list.append(cnt)

    else :
        _list.append(cnt)
        cnt = 1

if n == 1 :
    print(1)

else :
    print(max(_list))

    

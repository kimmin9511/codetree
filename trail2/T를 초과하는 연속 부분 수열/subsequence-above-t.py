n, t = map(int, input().split())
arr = list(map(int, input().split()))

cnt = 0

_list = []

for i in range(n) :

    if arr[i] > t :
        
        if i == n-1 :
            cnt += 1
            _list.append(cnt)

        else :
            if arr[i+1] > t :
                cnt += 1

            else :
                cnt += 1
                _list.append(cnt)
                cnt = 0
    
    else :
        _list.append(cnt)
        cnt = 0

print(max(_list))




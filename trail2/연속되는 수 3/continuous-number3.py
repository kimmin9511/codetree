N = int(input())
arr = [int(input()) for _ in range(N)]

cnt = 0
_list = []

for i in range(N) :
    if i == 0 or (arr[i] < 0 and arr[i-1] < 0) or (arr[i] > 0 and arr[i-1] > 0) :
        cnt += 1

        if i == N-1 :
            _list.append(cnt)

    else :
        _list.append(cnt)
        cnt = 1

print(max(_list))



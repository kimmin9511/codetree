N, K, P, T = map(int, input().split())
handshakes = [tuple(map(int, input().split())) for _ in range(T)]

handshakes.sort(key = lambda x : x[0])


_list = [0] * 101
_list[P] = 1

_num = [0] * 101
_num[P] = K

for i in handshakes :
    if _list[i[1]] == 1 or _list[i[2]] == 1 :
        if _list[i[1]] == 1 and _list[i[2]] != 1 and _num[i[1]] > 0 :

            _list[i[2]] = 1
            _num[i[2]] = K
            _num[i[1]] -= 1

        elif _list[i[1]] != 1 and _list[i[2]] == 1 and _num[i[2]] > 0 :

            _list[i[1]] = 1
            _num[i[1]] = K
            _num[i[2]] -= 1

        elif _list[i[1]] == 1 and _list[i[2]] == 1 :
            if _num[i[1]] > 0 :
                _num[i[1]] -= 1

            if _num[i[2]] > 0 :
                _num[i[2]] -= 1

for j in _list[1:N+1] :
    print(j, end="")



    

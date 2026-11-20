N, M, K = map(int, input().split())
student = [int(input()) for _ in range(M)]

_list = [0] * N

num = -1

for i in student :
    _list[i-1] += 1

    if _list[i-1] >= K :
        num = i
        break

print(num)



    

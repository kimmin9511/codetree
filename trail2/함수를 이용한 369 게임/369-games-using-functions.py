a, b = map(int, input().split())

def first(i) :
    i = str(i)
    return '3' in i or '6'in i or '9' in i


def second(j) :
    return j % 3 == 0 or first(j) 


cnt = 0
for k in range(a, b+1) :
    if second(k) :
        cnt += 1

print(cnt)




    
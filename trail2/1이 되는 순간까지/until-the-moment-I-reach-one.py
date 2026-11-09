N = int(input())
cnt = 0

def f(k) :
    global cnt

    if k == 1 :
        return cnt

    elif k % 2 == 0 :
        cnt += 1
        return f(k/2)
    
    elif k % 2 == 1 :
        cnt += 1
        return f(k//3)

    
print(f(N))
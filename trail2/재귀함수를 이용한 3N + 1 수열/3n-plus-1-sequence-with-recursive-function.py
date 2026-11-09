n = int(input())

def f(k) :

    if k == 1 :
        return 0

    if k % 2 == 0 :
        return f(k/2) + 1

    elif k % 2 == 1 :
        return f(k*3+1) + 1


print(f(n))
N = int(input())


def f(k) :
    if k == 1 :
        return 1

    if k == 2 :
        return 2

    return f(k//3) + f(k-1) 


print(f(N))
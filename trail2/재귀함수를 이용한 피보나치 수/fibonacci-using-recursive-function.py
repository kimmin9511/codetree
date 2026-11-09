N = int(input())


def f(k) :
    if k == 1 :
        return 1

    if k == 2 :
        return 1

    return f(k-1) + f(k-2)

    
print(f(N))
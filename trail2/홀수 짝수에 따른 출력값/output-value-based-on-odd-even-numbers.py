N = int(input())

def f(k) :
    if k % 2 == 1 :
        if k == 1 :
            return 1

        return f(k-2) + k

    elif k % 2 == 0 :
        if k == 2 :
            return 2

        return f(k-2) + k


print(f(N))
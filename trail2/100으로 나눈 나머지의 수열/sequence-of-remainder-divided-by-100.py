N = int(input())


def f(k) :
    if k == 1 :
        return 2

    if k == 2 :
        return 4

    return (f(k-1) * f(k-2)) % 100


print(f(N))
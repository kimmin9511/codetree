N = int(input())


def num(k) :
    if k == 0 :
        return

    print(k, end=" ")
    num(k-1)
    print(k, end=" ")


num(N)
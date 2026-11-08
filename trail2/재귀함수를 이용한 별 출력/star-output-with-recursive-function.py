n = int(input())


def line(k) :
    if k == 0 :
        return

    line(k-1)
    print("*" * k)

line(n)
n = int(input())


def star(k) :
    if k == 0 :
        return

    print("* " * k)
    star(k-1)
    print("* " * k)


star(n)
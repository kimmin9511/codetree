a, b = map(int, input().split())


def add_or_multiple(n, m) :
    if n > m :
        n += 25
        m *= 2

    else :
        n *= 2
        m += 25

    return n, m

a, b = add_or_multiple(a, b)
print(a, b)
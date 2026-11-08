n = int(input())


def word(k) :
    if k == 0 :
        return

    word(k-1)
    print("HelloWorld")

word(n)
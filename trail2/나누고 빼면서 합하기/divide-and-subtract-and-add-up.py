n, m = map(int, input().split())
A = list(map(int, input().split()))
sum = 0


def plus() :
    global m
    global sum


    while (m != 1) :
        sum += A[m-1]
        if m % 2 == 0 :
            m = int(m/2)

        elif m % 2 == 1 :
            m -= 1


    sum += A[0]
    return sum



print(plus())
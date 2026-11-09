N = int(input())

def fact(k) :
    if k == 1:
        return 1

    return fact(k-1)*k


print(fact(N))
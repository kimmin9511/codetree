N = int(input())

def fact(k) :
    if k < 10 :
        return k*k

    return fact(k//10) + (k%10)*(k%10)


print(fact(N))



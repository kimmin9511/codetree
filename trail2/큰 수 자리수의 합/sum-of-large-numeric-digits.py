a, b, c = map(int, input().split())

num = a*b*c

def f(k) :
    if k < 10 :
        return k % 10

    return f(k//10) + (k%10)


print(f(num))
n = int(input())
arr = list(map(int, input().split()))

def gcd(a, b) :
    if b == 0 :
        return a

    return gcd(b, a%b)


def lcm(c, d) :

    return (c*d) // gcd(c, d)


def num(k) :
    if k == 1 :
        return arr[0]

    return lcm(num(k-1), arr[k-1])


print(num(n))
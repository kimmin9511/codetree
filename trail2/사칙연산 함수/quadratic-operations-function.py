a, o, c = input().split()
a = int(a)
c = int(c)

def plus(n, m) :
    return n+m

def minus(n,m) :
    return n-m

def multiple(n, m) :
    return n*m

def division(n, m) :
    return n//m

if o == '+' :
    print(f"{a} + {c} = {plus(a, c)}")

elif o == '-' :
    print(f"{a} - {c} = {minus(a, c)}")

elif o == '*' :
    print(f"{a} * {c} = {multiple(a, c)}")

elif o == '/' :
    print(f"{a} / {c} = {division(a, c)}")

else :
    print("False")
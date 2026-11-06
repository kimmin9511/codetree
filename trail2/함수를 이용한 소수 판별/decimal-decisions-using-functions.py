a, b = map(int, input().split())

def prime(n) :
    for i in range(2, n) :
        if n % i == 0 :
            return False
                
    return True


sum = 0
for k in range(a, b+1) :
    if prime(k) :
        sum += k

print(sum)


    
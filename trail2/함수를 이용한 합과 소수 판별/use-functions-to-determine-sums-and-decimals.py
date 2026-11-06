a, b = map(int, input().split())

def prime(k) :
    for i in range(2, k) :
        if k % i == 0 :
            return False

    return True


def count(n) :
    if ((n//10) + (n%10)) % 2 == 0 :
        return True

    return False


cnt = 0
for i in range(a, b+1) :
    if prime(i) and count(i) :
        cnt += 1

print(cnt)


n, m = map(int, input().split())

def print_max(a, b) :
    max_num = 1
    if a > b :
        for i in range(1, a+1) :
            if a % i == 0 and b % i == 0 :
                max_num = i

    elif b > a :
        for j in range(1, b+1) :
            if a % j == 0 and b % j == 0 :
                max_num = j

    else :
        max_num = a

    print(max_num)


print_max(n, m)
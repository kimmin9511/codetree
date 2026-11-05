n, m = map(int, input().split())


def print_min(a, b) :
    num = 1
    if a > b :
        while (a*num) % b != 0 :
            num += 1
        print(a*num)

    elif a < b :
        while (b*num) % a != 0 :
            num += 1
        print(b*num)
    
    else :
        print(a)
    


print_min(n, m)
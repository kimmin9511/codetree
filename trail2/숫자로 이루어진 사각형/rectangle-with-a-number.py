n = int(input())

def print_number(a, num) :
    for _ in range(a) :
        for _ in range(a) :
            print(num, end=" ")
            num += 1

            if num > 9 :
                num = 1
        print()


print_number(n, 1)

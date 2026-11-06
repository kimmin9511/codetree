M, D = map(int, input().split())


def year(a, b) :
    if 1<= a <= 12 :
        if a == 2 :
            if 1<= b <= 28 :
                return True

        elif a == 4 or a == 6 or a == 9 or a == 11 :
            if 1<= b <= 30 :
                return True

        else :
            if 1<= b <= 31 :
                return True

    return False


if year(M, D) :
    print("Yes") 

else :
    print("No")
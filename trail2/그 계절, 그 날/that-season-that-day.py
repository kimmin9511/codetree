Y, M, D = map(int, input().split())

# 윤년인지 아닌지를 판단하는 함수
def yoon(a) :
    if a % 4 == 0 :
        if a % 100 == 0 :
            if a % 400 == 0 :
                return True
            return False
        return True
    return False


# 윤년이라면 2월은 29일까지, 윤년이 아니라면 2월은 28일까지
def season(a, b, c) :
    if yoon(a) :
        if 1<=b<=12 :
            if b == 2 :
                if 1<=c<=29 :
                    return True

            elif b == 4 or b == 6 or b == 9 or b == 11 :
                if 1<=c<=30 :
                    return True

            else :
                if 1<=c<=31 :
                    return True

        return False

    else :
        if 1<=b<=12 :
            if b == 2 :
                if 1<=c<=28 :
                    return True

            elif b == 4 or b == 6 or b == 9 or b == 11 :
                if 1<=c<=30 :
                    return True

            else :
                if 1<=c<=31 :
                    return True

        return False


# True or False값에 따라 False면 -1 출력, True면 해당 월이 봄 여름 가을 겨울 중에 어느 계절인지 확인하고 프린트.
if season(Y, M, D) :
    if 3<=M<=5 :
        print("Spring")

    elif 6<=M<=8 :
        print("Summer")

    elif 9<=M<=11 :
        print("Fall")

    elif M == 12 or M == 1 or M == 2 :
        print("Winter")

else :
    print(-1)




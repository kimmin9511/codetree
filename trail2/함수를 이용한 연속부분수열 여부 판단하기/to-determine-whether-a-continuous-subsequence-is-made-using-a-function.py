n1, n2 = map(int, input().split())
a = list(map(int, input().split()))
b = list(map(int, input().split()))



def part(n, m) :
    for i in range(0, n-m+1, 1) :
        cnt = 0
        if a[i] == b[0] :
            for j in range(m) :
                if a[i+j] == b[j] :
                    cnt += 1

            if cnt == m :
                return True

            else :
                continue


    return False


if part(n1, n2) :
    print("Yes")

else :
    print("No")




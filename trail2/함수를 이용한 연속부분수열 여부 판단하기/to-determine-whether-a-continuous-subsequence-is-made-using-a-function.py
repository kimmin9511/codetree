n1, n2 = map(int, input().split())
a = list(map(int, input().split()))
b = list(map(int, input().split()))


# cnt 위치 주의 ! 첫번째거가 일치해서 비교해보다가 다르면 continue로 다시 넘어오기 때문에 cnt도 초기화를 해줘야함. for문 안에 위치하도록 조정.

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




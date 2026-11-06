n = int(input())

# 2자리 숫자, 10으로 나눈 몫과 10으로 나눈 나머지의 합이 5 or 10 -> 5의 배수

def find_num(k) :
    return k % 2 == 0 and ((k//10) + (k%10)) % 5 == 0


if find_num(n) :
    print("Yes")

else :
    print("No")
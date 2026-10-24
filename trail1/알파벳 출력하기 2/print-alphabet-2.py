n = int(input())
num = 65

for i in range(n) :
    for j in range(i) :
        print(" ", end=" ")

    for j in range(n-i) :
        print(chr(num), end=" ")
        num+=1
        if num > 90 :
            num = 65

    print()
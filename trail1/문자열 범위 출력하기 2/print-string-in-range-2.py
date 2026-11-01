str = input()
num = int(input())

if num > len(str) :
    for i in range(-1, -1*len(str)-1, -1) :
        print(str[i], end="")

else :
    for i in range(-1, -1*num-1, -1) :
        print(str[i], end="")

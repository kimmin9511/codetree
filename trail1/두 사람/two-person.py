a, b = map(str, input().split())

x, y = map(str, input().split())

if int(a) >= 19 and int(x) >= 19 :
    if b == "M" or y == "M" :
        print(1)
    
    else :
        print(0)

elif int(a) >= 19 :
    if b == "M" :
        print(1)
    
    else :
        print(0)

elif int(x) >= 19 :
    if y == "M" :
        print(1)

    else :
        print(0)

else :
    print(0)
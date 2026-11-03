a, b = map(str, input().split())

if a.isdigit() == True :
    a = int(a)

else :
    for i in a :
        if i.isdigit() == False :
            a = list(a)
            a = a[:a.index(i)]
            a = ''.join(a)
            a = int(a)
            break

if b.isdigit() == True :
    b = int(b)

else :
    for i in b :
        if i.isdigit() == False :
            b = list(b)
            b = b[:b.index(i)]
            b = ''.join(b)
            b = int(b)
            break


print(a+b)
    
    
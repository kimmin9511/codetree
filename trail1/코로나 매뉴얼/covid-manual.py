a, b = map(str, input().split())
c, d = map(str, input().split())
e, f = map(str, input().split())

x = 0
y = 0

if a == "Y" :
    if int(b) >= 37 :
        x+=1

    else :
        y+=1
else : 
    y+=1

if c == "Y" :
    if int(d) >= 37 :
        x+=1

    else :
        y+=1
else : 
    y+=1

if e == "Y" :
    if int(f) >= 37 :
        x+=1

    else :
        y+=1
else : 
    y+=1

if x>=2:
    print("E")

else :
    print("N")
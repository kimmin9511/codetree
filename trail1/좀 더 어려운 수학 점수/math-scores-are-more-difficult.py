a, b = map(int, input().split())

x, y = map(int, input().split())

if a == x :
    if b > y :
        print("A")
    
    else :
        print("B")

elif a > x :
    print("A")

else :
    print("B")
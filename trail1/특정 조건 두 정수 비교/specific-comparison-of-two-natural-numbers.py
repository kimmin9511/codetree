a, b = map(int, input().split())
x, y = 0, 0

if a < b :
    x = 1

else : 
    x = 0

if a == b:
    y = 1

else :
    y = 0

print(x, y)
    
import sys

n = list(map(int, input().split()))

max_val = -sys.maxsize

for i in n :
    if i > max_val :
        max_val = i

    
print(max_val)
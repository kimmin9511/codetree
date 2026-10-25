n = int(input())
a = list(map(int, input().split()))

for i in range(n) :
    b = [i**2 for i in a]

for i in b :
    print(i, end=" ")


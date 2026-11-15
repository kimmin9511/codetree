N, B = map(int, input().split())

digit = []

while True :
    if N < 1 :
        break

    digit.append(N%B)
    N //= B

for i in digit[::-1]:
    print(i, end="")

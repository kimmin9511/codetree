a = input()
b = input()
cnt = -1

for i in range(1, len(a)+1) :
    b = b[1:] + b[0]

    if a == b :
        cnt = i
        break

print(cnt)

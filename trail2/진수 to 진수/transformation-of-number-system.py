a, b = map(int, input().split())
n = input()

digit = []

for i in range(len(n)) :
    digit.append(n[i])

num = 0
for j in range(len(digit)) :
    num = num * a + int(digit[j])

solve = []

while True :
    if a == b :
        print(n)
        break
        
    if b == 2 :
        if num < 2 :
            solve.append(num)
            break

    else :
        if num < 1 :
            break

    solve.append(num%b)
    num //= b

for k in solve[::-1] :
    print(k, end="")
            
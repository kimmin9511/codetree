N = input()

digit = []
num = 0

for i in range(len(N)) :
    digit.append(N[i])

for j in range(len(digit)) :
    num = num * 2 + int(digit[j])

num *= 17
solve = []

while True :
    if num < 2 :
        solve.append(num)
        break

    solve.append(num%2)
    num //= 2


for k in solve[::-1] :
    print(k, end="")


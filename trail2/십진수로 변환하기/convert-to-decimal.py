binary = input()

num = 0
digit = []

for i in binary :
    digit.append(i)

for j in range(len(digit)) :
    num = num * 2 + int(digit[j])

print(num)
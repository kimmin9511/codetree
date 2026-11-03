a = input()
b = input()

arr_a, arr_b = [], []

for i in a :
    if i.isdigit() == True :
        arr_a.append(i)

for j in b :
    if j.isdigit() == True :
        arr_b.append(j)

num_a = int(''.join(arr_a))
num_b = int(''.join(arr_b))

print(num_a + num_b)
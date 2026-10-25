a, b = map(int, input().split())

arr = [0 for _ in range(10)]
new_arr = []

while True :
    if a == 1 or a == 0 :
        break

    c = a%b
    a //= b
    arr[c] += 1

for i in range(10) :
    new_arr.append(arr[i]**2)

print(sum(new_arr))




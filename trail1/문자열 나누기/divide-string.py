n = int(input())

num = list(map(str, input().split()))

num_val = "".join(num)

for i in range(1, len(num_val)+1) :
    print(num_val[i-1], end="")

    if i % 5 == 0 :
        print()
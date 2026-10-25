n = int(input())

m = list(map(float, input().split()))

val = 0

for i in range(n) :
    val += m[i]

print(f"{(val/n):.1f}")

if val/n >= 4.0 :
    print("Perfect")

elif val/n >= 3.0 :
    print("Good")

else :
    print("Poor")
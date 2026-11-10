n = int(input())
A = list(map(int, input().split()))
B = list(map(int, input().split()))


A.sort()
B.sort()

torf = True

for i in range(len(A)) :
    if A[i] != B[i] :
        torf = False

if torf :
    print("Yes")

else :
    print("No")


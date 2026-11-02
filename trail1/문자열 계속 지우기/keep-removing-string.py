A = input()
B = input()

a = len(A)
b = len(B)

while True:
    idx = -1
    for i in range(a - b + 1):
        is_same = True

        for j in range(b):
            if A[i + j] != B[j]:
                is_same = False
                break
        
        if is_same:
            idx = i
            break

    if idx == -1:
        break

    A = A[:idx] + A[idx + b:]

    a = len(A)

print(A)

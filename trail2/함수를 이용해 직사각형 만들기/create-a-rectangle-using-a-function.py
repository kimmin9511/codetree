n, m = map(int, input().split())

def print_1(row, col) :
    for _ in range(row) :
        print("1" * col)

print_1(n, m)
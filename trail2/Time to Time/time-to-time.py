a, b, c, d = map(int, input().split())

start_min = a*60 + b
final_min = c*60 + d

print(final_min - start_min)
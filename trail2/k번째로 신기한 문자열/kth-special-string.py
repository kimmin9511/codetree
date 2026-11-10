n, k, t = input().split()
n, k = int(n), int(k)
str = [input() for _ in range(n)]

arr = []

for word in str :
    if word[0:len(t)] == t[0:len(t)] :
        arr.append(word)

arr.sort()

print(arr[k-1])
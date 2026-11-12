n = int(input())
name = []
address = []
region = []

for _ in range(n):
    name_value, address_value, region_value = input().split()
    name.append(name_value)
    address.append(address_value)
    region.append(region_value)


class info :
    def __init__(self, a, b, c) :
        self.name = a
        self.address = b
        self.region = c


name2 = sorted(name)

k = name2[-1]

for i in name :
    if i == k :
        num = name.index(i)

human_info = info(name[num], address[num], region[num])

print(f"name {human_info.name}")
print(f"addr {human_info.address}")
print(f"city {human_info.region}")
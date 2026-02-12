n = int(input())
name = []
street_address = []
region = []

for _ in range(n):
    n_i, s_i, r_i = input().split()
    name.append(n_i)
    street_address.append(s_i)
    region.append(r_i)

# Please write your code here.
class Personal:
    def __init__(self, name, address, region):
        self.name = name
        self.address = address
        self.region = region

persons = [Personal(n, s, r) for n, s, r in zip(name, street_address, region)]
persons.sort(key=lambda person:person.name)
slow = persons[-1]
print(f'name {slow.name}')
print(f'addr {slow.address}')
print(f'city {slow.region}')

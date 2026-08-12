
from collections import OrderedDict

n = int(input())

items = OrderedDict()

for i in range(n):
    name, price = input().rsplit(" ", 1)
    price = int(price)

    if name in items:
        items[name] += price
    else:
        items[name] = price

for name, price in items.items():
    print(name, price)
from collections import Counter

num_shoes = int(input())
sizes = list(map(int, input().split()))
stock = Counter(sizes)

num_customers = int(input())
earned = 0

for i in range(num_customers):
    size, price = map(int, input().split())
    if stock[size] > 0:
        earned += price
        stock[size] -= 1

print(earned)
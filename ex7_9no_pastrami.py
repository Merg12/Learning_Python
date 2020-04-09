sandwich_orders = ['cheese', 'pastrami', 'meatball', 'ham', 'pastrami', 'pastrami']

print(sandwich_orders)

print("We are out of Pastrami")

while 'pastrami' in sandwich_orders:
    sandwich_orders.remove('pastrami')

print(sandwich_orders)
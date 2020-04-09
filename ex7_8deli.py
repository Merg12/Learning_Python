sandwich_orders = ['cheese', 'meatball', 'ham']
finished_sandwichs = []

print("\nworking on:")

while sandwich_orders:
    current_sandwich = sandwich_orders.pop()

    finished_sandwichs.append(current_sandwich)
    print(current_sandwich)

print("\nsandwiches ready:")

for finished_sandwich in finished_sandwichs:
    print(finished_sandwich)